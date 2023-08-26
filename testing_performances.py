import numpy as np
import argparse
import random
import pandas as pd
import torch
import torchvision.transforms as transforms
from copy import deepcopy
from torch.utils.data import DataLoader
from help_code_demo1 import ToTensor, IEGM_DataSET, F1, FB, Sensitivity, Specificity, BAC, ACC, PPV, NPV

def main():
    seed = 222
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

    # Hyperparameters
    BATCH_SIZE_TEST = 1
    SIZE = args.size
    path_data = args.path_data
    path_records = args.path_record
    path_net = args.path_net
    path_indices = args.path_indices


    test_indice_path = args.path_indices + 'test_indice.csv'
    test_indices = pd.read_csv(test_indice_path)  # Adjust delimiter if necessary

    subjects = test_indices['Filename'].apply(lambda x: x.split('-')[0]).unique().tolist()

    # List to store metrics for each participant
    subject_metrics = []

    # Load trained network
    net = torch.load(path_net + 'IEGM_net.pkl')
    net.eval()
    net.cuda()
    device = torch.device('cuda:0')
    subjects_above_threshold = 0

    for subject_id in subjects:
        testset = IEGM_DataSET(root_dir=path_data,
                               indice_dir=path_indices,
                               mode='test',
                               size=SIZE,
                               subject_id=subject_id,
                               transform=transforms.Compose([ToTensor()]))

        testloader = DataLoader(testset, batch_size=BATCH_SIZE_TEST, shuffle=True, num_workers=0)

        segs_TP = 0
        segs_TN = 0
        segs_FP = 0
        segs_FN = 0


        for data_test in testloader:
            IEGM_test, labels_test = data_test['IEGM_seg'], data_test['label']
            seg_label = deepcopy(labels_test)

            IEGM_test = IEGM_test.float().to(device)
            labels_test = labels_test.to(device)

            outputs_test = net(IEGM_test)
            _, predicted_test = torch.max(outputs_test.data, 1)

            if seg_label == 0:
                segs_FP += (labels_test.size(0) - (predicted_test == labels_test).sum()).item()
                segs_TN += (predicted_test == labels_test).sum().item()
            elif seg_label == 1:
                segs_FN += (labels_test.size(0) - (predicted_test == labels_test).sum()).item()
                segs_TP += (predicted_test == labels_test).sum().item()

        # Calculate metrics for the current participant
        f1 = round(F1([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        fb = round(FB([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        se = round(Sensitivity([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        sp = round(Specificity([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        bac = round(BAC([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        acc = round(ACC([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        ppv = round(PPV([segs_TP, segs_FN, segs_FP, segs_TN]), 5)
        npv = round(NPV([segs_TP, segs_FN, segs_FP, segs_TN]), 5)

        # Check if F-beta score exceeds 0.95



        # Append metrics to the subject_metrics list
        subject_metrics.append([f1, fb, se, sp, bac, acc, ppv, npv])
        if fb > 0.95:
            subjects_above_threshold += 1

    # Convert the list of lists to a NumPy array for easier calculations
    subject_metrics_array = np.array(subject_metrics)

    # Calculate the mean values along the rows (subjects)
    average_metrics = np.mean(subject_metrics_array, axis=0)

    # Extract the individual average metric values
    avg_f1, avg_fb, avg_se, avg_sp, avg_bac, avg_acc, avg_ppv, avg_npv = average_metrics

    avg_f1 = round(avg_f1, 5)
    avg_fb = round(avg_fb, 5)
    avg_se = round(avg_se, 5)
    avg_sp = round(avg_sp, 5)
    avg_bac = round(avg_bac, 5)
    avg_acc = round(avg_acc, 5)
    avg_ppv = round(avg_ppv, 5)
    avg_npv = round(avg_npv, 5)

    # Print average metric values
    print("Final F-1:", avg_f1)
    print("Final F-B:", avg_fb)
    print("Final SEN:", avg_se)
    print("Final SPE:", avg_sp)
    print("Final BAC:", avg_bac)
    print("Final ACC:", avg_acc)
    print("Final PPV:", avg_ppv)
    print("Final NPV:", avg_npv)

    # Calculate the proportion of subjects above the threshold
    proportion_above_threshold = subjects_above_threshold / len(subjects)

    # The G score
    g_score = proportion_above_threshold

    # Print the G score
    print("G Score:", g_score)

    f = open(path_records + 'seg_stat.txt', 'a')
    f.write("Final F-1: {}\n".format(avg_f1))
    f.write("Final F-B: {}\n".format(avg_fb))
    f.write("Final SEN: {}\n".format(avg_se))
    f.write("Final SPE: {}\n".format(avg_sp))
    f.write("Final BAC: {}\n".format(avg_bac))
    f.write("Final ACC: {}\n".format(avg_acc))
    f.write("Final PPV: {}\n".format(avg_ppv))
    f.write("Final NPV: {}\n\n".format(avg_npv))
    f.write("G Score: {}\n".format(g_score))
    f.close()

    del net

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--cuda', type=int, default=0)
    argparser.add_argument('--size', type=int, default=1250)
    argparser.add_argument('--path_data', type=str, default='H:/Date_Experiment/data_IEGMdb_ICCAD_Contest/segments-R250'
                                                            '-BPF15_55-Noise/tinyml_contest_data_training/')
    argparser.add_argument('--path_net', type=str, default='./saved_models/')
    argparser.add_argument('--path_record', type=str, default='./records/')
    argparser.add_argument('--path_indices', type=str, default='./data_indices/')

    args = argparser.parse_args()

    device = torch.device("cuda:" + str(args.cuda))
    print("device is --------------", device)

    main()