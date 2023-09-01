# Getting Start with STM32CubeAI

  ### Environment

  1. STM32CubeMX

     https://www.st.com/en/development-tools/stm32cubemx.html

     Availability as standalone software running on Windows®, Linux® and macOS® operating systems and 64-bit Java Runtime environment.

  2. MDK5

  3. ST-Link driver

     https://www.st.com/content/my_st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-link009.license=1656325086116.product=STSW-LINK009.version=2.0.2.html

  4. STM32L031K6T6

     Arm Cortex-M0+ core at 32 MHz

     32 Kbytes of Flash memory, 8 Kbytes of SRAM

     Embedded ST-Link/V2-1 debugger/programmer

     ![L031K6T6](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/STM32L031K6T6.png)

  

  ### New Project

  1. Open STM32CubeMX and click ***ACCESS TO BOARD SELECTER*** and select our board.

     ![mainmenu](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/mainmenu.png)

     ![select board](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/2.png)

  2. Click ***Software Packs --- Manage Software Packs*** and 

     ![manage software packs](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/3.png)

     Click the check box of <u>Artifacial Intelligence( v7.1.0 )</u> under **X.CUBE.AI** and click ***Install Now.***

     ![install](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/4.png)

  3. Click ***Software Packs --- Select Components*** and set option as follow.

     ![components](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/5.png)

     ![Snipaste_2022-07-09_16-19-42](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/6.png)

  4. Set PA2 as VCP_TX, and set PA15 as VCP_RX.

     ![pins](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/7.png)

  5. Set Connectivity.

     ![connectivity](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/8.png)

  6. Set AI network

     First, set the communication options as follow

     ![plantform setting](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/9.png)

     Then click ***Add network*** and import ours model by follow steps shown in the picture.

     ![image-20220627201730152](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/10.png)

     After choosing model, you can click ***Analyze*** to view the resources needed to run the model.

     ![image-20220627202020441](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/11.png)

  7. Set Clock

     ![clock](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/12.png)

  8. Finish settings and click ***GENERATE CODE***

     ![project manager](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/13.png)

  ## Load Program to Board

  1. Connet the boadr to computer.

     <img src="https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/15l.jpg" alt="image-20220627203515997" style="zoom: 25%;" />

  2. Open project in MDK5 and build.
      First, Check the ***startup_stm32f303x8.s*** file.
         ![build](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/110.png)

      Then，build the project.
     ![build](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/14.png)

  3. Check if the debugger is connected.

     First, click ***Options for Target***.

     ![targets](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/16.png)

     Then switch to <u>Debug</u> and click ***Settings***.

     <img src="https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/17.png" alt="debug"  />

     If the debugger is connected, you can see the IDCODE and the Device Name. 

     <img src="https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/18.png" alt="swdio"  />

     Finally, switch to <u>Flash Download</u> and check <u>Reset and Run</u>

     ![full chip](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/19.png)

  4. Now you can load program to the board.

     ![load](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/20.png)

  ## Validation

  1. Click the reset button on the bottom of the board.

     ![image-20220627203955477](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/21.png)

  2. Open CUbeMX project that we built before and switch to <u>network</u>

     ![image-20220627204238965](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/22l.png)

  3. Click ***Validate on target*** and you can see how the model runs on the board.

     ![image-20220627204444260](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/23.png)

     ![image-20220627204542939](https://raw.githubusercontent.com/zhuiyi1314/TinyML/main/img/24.png)

 
 ## Metrics
 
 Two metrics, **Used Flash** and **duration**, will be extracted as the metrics to report the final scoring. 