class RECEIVERELE:
    testcase1 = {
        # 进入receiver 页面id
        "1": 'com.runcam.android.runcambf:id/receiver_icon',

        # 接收机类型
        "2": '//android.widget.TextView[@resource-id="android:id/text1" and @text="串行接收机 (通过UART)"]',
        "3": '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="PPM/CPPM (单线)"]',
        "4": '//android.view.View[@resource-id="com.runcam.android.runcambf:id/telemetry_switch"]',
    }

