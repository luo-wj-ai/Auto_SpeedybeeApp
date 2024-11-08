class RECEIVERELE:
    testcase1 = {
        # 进入receiver 页面id
        "1": 'com.runcam.android.runcambf:id/receiver_icon',

        # 接收机类型
        "2": '//android.widget.TextView[@resource-id="android:id/text1" and @text="串行接收机 (通过UART)"]',
        "3": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="PPM/CPPM (单线)"]',
        "4": '//android.view.View[@resource-id="com.runcam.android.runcambf:id/telemetry_switch"]',

        # rolling start
        "5": '//android.widget.TextView[@text="遥测输出"]',
        # rolling end
        "6": '(//android.widget.ProgressBar[@resource-id="com.runcam.android.runcambf:id/channels_progressBar"])[2]',

        "7": '//android.view.View[@resource-id="com.runcam.android.runcambf:id/rssi_switch"]',

        "8": '//android.widget.TextView[@resource-id="android:id/text1" and @text="已禁用"]',

        # rolling start
        "9": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="AUX 9"]',
        # rolling end
        "10": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="AUX 6"]',

        "11": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="AUX 12"]',

        # 参数值输入
        "12": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1050"]',
        "13": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "14": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "15": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "16": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "17": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "18": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "19": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1500"]',
        "20": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "21": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "22": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "23": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "24": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "25": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "26": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1900"]',
        "27": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "28": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "29": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "30": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "31": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num3"]',
        "32": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num3"]',
        "33": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num3"]',
        "34": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num3"]',
        "35": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "36": '(//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent"])[4]',
        "37": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num3"]',
        "38": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num2"]',
        "39": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "40": '(//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent"])[5]',
        "41": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "42": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "43": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "44": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "45": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="50"]',
        "46": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "47": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "48": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "49": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        # rolling start
        "50": '//android.widget.TextView[@text="RC平滑"]',
        # rolling end
        "51": '//android.widget.TextView[@text="通道映射"]',

        "52": '//android.widget.TextView[@resource-id="android:id/text1" and @text="开"]',
        "53": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="关"]',
        "54": '//android.widget.TextView[@resource-id="android:id/text1" and @text="20 ms"]',
        "55": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="250 ms"]',

        # save & restart
        "56": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/save_and_reboot_btn"]'
    }

    testcase2 = {
        # 进入receiver 页面id
        "1": 'com.runcam.android.runcambf:id/receiver_icon',

        # 接收机类型
        "2": '//android.widget.TextView[@resource-id="android:id/text1" and @text="串行接收机 (通过UART)"]',
        "3": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="SPI接收机 (例如内置RX)"]',

        # rolling start
        "4": '(//android.widget.TextView[@text="TELEMETRY"])[1]',
        # rolling end
        "5": '(//android.widget.ProgressBar[@resource-id="com.runcam.android.runcambf:id/channels_progressBar"])[2]',

        # "6": '//android.widget.FrameLayout[@resource-id="com.runcam.android.runcambf:id/right_content_fl"]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView',        # 不可点击

        # "7": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Spektrum/Graupner/JR (TAER1234)"]',


        # 参数值输入
        "8": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1050"]',
        "9": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "10": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "11": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "12": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "13": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "14": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num2"]',
        "15": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "16": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "17": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "18": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1500"]',
        "19": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "20": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "21": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "22": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "23": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "24": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num6"]',
        "25": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "26": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "27": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "28": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="1900"]',
        "29": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "30": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "31": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "32": '//android.widget.ImageView[@resource-id="com.runcam.android.runcambf:id/input_delete_img"]',
        "33": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num1"]',
        "34": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num8"]',
        "35": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "36": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "37": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "38": '(//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent"])[4]',
        "39": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "40": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "41": '(//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent"])[5]',
        "42": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num5"]',
        "43": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "44": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        "45": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/tvStepperContent" and @text="50"]',
        "46": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num8"]',
        "47": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_num0"]',
        "48": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/input_finish"]',

        # rolling start
        "49": '//android.widget.TextView[@text="3D油门死区"]',
        # rolling end
        "50": '//android.widget.TextView[@text="模拟RSSI输入"]',

        "51": '(//android.widget.TextView[@resource-id="android:id/text1"])[2]',
        "52": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="手动"]',
        "53": '(//android.widget.LinearLayout[@resource-id="com.runcam.android.runcambf:id/ivStepperPlus"])[4]/android.widget.ImageView',    # 不可点击

        "54": '//android.widget.TextView[@resource-id="android:id/text1" and @text="自动"]',
        "55": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="手动"]',
        "56": '(//android.widget.LinearLayout[@resource-id="com.runcam.android.runcambf:id/ivStepperPlus"])[5]/android.widget.ImageView',    # 不可点击
        "57": '(//android.widget.LinearLayout[@resource-id="com.runcam.android.runcambf:id/ivStepperPlus"])[5]/android.widget.ImageView',    # 不可点击
        "58": '(//android.widget.LinearLayout[@resource-id="com.runcam.android.runcambf:id/ivStepperPlus"])[5]/android.widget.ImageView',    # 不可点击


        "59": '//android.widget.TextView[@resource-id="android:id/text1" and @text="20 ms"]',
        "60": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="10 ms"]',

        # save & restart
        "61": '//android.widget.TextView[@resource-id="com.runcam.android.runcambf:id/save_and_reboot_btn"]'
    }

