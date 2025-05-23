# Speedybee—自动化测试

### 一、简要框架介绍
```
Approach：通用方法使用
Element：元素
Result：测试报告
test_case：测试用例
```
---
### 二、Github拉取项目代码
```
远程仓库：git remote add origin https://github.com/luo-wj-ai/SpeedybeeApp.git
重命名master分支：git branch -M main
将本地的"main"分支推送到远程仓库"origin"：git push -u origin main

#push代码
git add .
git commit -m "这里面是你需要写的内容"
git push

#pull拉取代码
git pull

#分支
建立分支：git branch iOS
切换分支：git checkout iOS
合并分支：git merge iOS
删除分支：git branch -d iOSexit
```
---
### 三、运行项目
1. 命令行： python -m unittest -v yourfile.py
2. 参考：https://www.cnblogs.com/youreyebows/p/7867508.html
---
### 四、页面详细测试
| BF页面  | 英文         | 操作步骤01                                      | 操作步骤02 |
|:------|:-----------|:--------------------------------------------|:-----------|
| 设置    | Setup      | 恢复默认设置                                      |            |
| 预设    | Presets    | 选择固件4.5-an进行预设                               |            |
| 端口    | Port       | 打开UART2-MSP<br/>UART3-串行接收机<br/>UART4-FrSky |            |
| 模式    | Mode       | 添加前四个范围和前3个链接                               |            |

### 五、测试动作

| Bee25 起飞参数设置页面 | 动作                                                                                                                                   |
| :--------------------- |:-------------------------------------------------------------------------------------------------------------------------------------|
| 设置                   | 校准加速度计                                                                                                                               |
| 端口                   | UART1-外围设备开启VTX(MSP+Displayport)<br>UART4-传感器开启GPS<br>UART6-串行接收机（略）                                                                 |
| 配置                   | 设置：<br>PID循环更新频率4.00kHz（略）<br>开启加速度计（略）<br>开启气压计（略）<br>其他功能：<br>开启GPS-OSD（略）                                                         |
| 电机                   | 设置：配置电机转向设置                                                                                                  |
| 接收机                 | 设置：<br>选择接收机类型：串行接收机（略）<br>接收机协议：CRSF（略）                                                                                             |
| OSD  | 开启：<br>--第一部分<br>G力<br>RSSI值<br>Tx上行链路功率<br>---第二部分<br>反乌龟模式翻转箭头<br>图传频道 |
| VTX                    | 加载图传表：IRC Tramp(USA)                                                                                                                 |
| GPS                    | 协议：UBLOX<br>自动设置：开启<br>使用Galileo系统：开启                                                                                                |
| 模式                   | 开启：<br>解锁-添加范围-AUX1<br>自稳模式-添加范围-AUX2                                                                                                |
### 六、实例JSON（动作）

~~~json
{
  "actions": [
    {
      "action": "click",
      "appby": "XPATH",
      "cond": "el",
      "ele": "//XCUIElementTypeButton[@name='登录']",
      "comment": "点击登录按钮"
    },
    {
      "action": "sendkeys",
      "appby": "ID",
      "cond": "el",
      "ele": "username_input",
      "keys": "test_user",
      "comment": "在用户名输入框输入用户名"
    },
    {
      "action": "clear",
      "appby": "ID",
      "cond": "el",
      "ele": "password_input",
      "comment": "清除密码输入框的内容"
    },
    {
      "action": "time",
      "duration": 3,
      "comment": "等待 3 秒"
    },
    {
      "action": "tap",
      "x_proportion": 0.5,
      "y_proportion": 0.8,
      "comment": "点击屏幕中间位置"
    },
    {
      "action": "swipe",
      "start_x": 0.1,
      "start_y": 0.5,
      "end_x": 0.9,
      "end_y": 0.5,
      "comment": "从左侧滑动到右侧"
    },
    {
      "action": "rolling",
      "start_locator_type": "XPATH",
      "start_locator": "//XCUIElementTypeCell[@name='起点']",
      "end_locator_type": "XPATH",
      "end_locator": "//XCUIElementTypeCell[@name='终点']",
      "cond": "el",
      "comment": "从起点滚动到终点"
    }
  ]
}



~~~
### 其他


#### 第一部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 1    | Aux 值              | G 力                    |
| 3    | GPS 卫星数          | GPS 维度                |
| 5    | GPS 经度            | GPS 速度                |
| 7    | PID 俯仰           | PID 方向                |
| 9    | PID 横滚           | RC 通道                 |
| 11   | RSNP 值            | RSSI 值                 |
| 13   | RTC 日期和时间      | Tx 上行链路功率         |
| 1AND15 | 上/下参考         | 先前 GPS 单圈时间       |

---

#### 第二部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 3    | 准备模式            | 功率                    |
| 5    | 十字准星            | 反乌龟模式翻转箭头    |
| 7    | 反重力              | 图传 DVR 状态           |
| 9    | 图传延迟            | 图传比特率              |
| 11   | 图传温度            | 图传电压                |
| 13   | 图传距离            | 图传频道                |
| 1AND15 | 实时电流          | 已上锁                  |

---

#### 第三部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 3    | 当前 GPS 单圈时间   | 接收机信号强度值         |
| 5    | 摄像头取景框         | 摇杆右折叠              |
| 7    | 摇杆左折叠           | 数字化 vario            |
| 9    | 数字化航向           | 张玉华 GPS 单圈时间     |
| 11   | 核心温度             | 模拟地平线              |
| 13   | 模拟地平线侧边栏     | 油门位置                |
| 1AND15 | 海拔高度          | 电机诊断                |

---

#### 第四部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 3    | 电池使用状态         | 电池已消耗电流           |
| 5    | 电池平均单芯电压     | 电池效率                 |
| 7    | 电池电压             | 电池电流功率消耗         |
| 9    | 电调温度             | 电调转速                 |
| 11   | 电调转速频率         | 罗盘标尺                 |
| 13   | 角度：俯仰          | 角度：横滚              |
| 1AND15 | 警告              | 计时器 1                |

---

#### 第五部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 3    | 计时器 2            | 经济时期：剩余时间估算    |
| 5    | 调整范围             | 调试                    |
| 7    | 起飞点方向           | 起飞点距离              |
| 9    | 连接信号质量         | 配置文件 OSD 配置文件名称|
| 11   | 配置文件 PID 和 Rate | 配置文件 PID 文件名称    |
| 13   | 配置文件 RATE 配置文件名称 | 飞手名称            |
| 1AND15 | 飞机名称          | 飞行总数                |

---

#### 第六部分
| 序号 | 字段 1               | 字段 2                   |
|------|---------------------|--------------------------|
| 3    | 飞行模式            | 飞行眼镜 DVR 状态        |
| 5    | 飞行眼镜信号质量     | 飞行眼镜电压             |
| 7    | 飞行眼镜系统警告     | 飞行眼镜风扇转速         |
| 9    | 飞行距离             | 黑匣子日志状态           |

## 参考网址
1. gitub项目源代码：[luo的gitub](https://github.com/luo-wj-ai/SpeedybeeApp)
2. CSDN博客参考
   3. [luo的Android](https://blog.csdn.net/Luoweijie42/article/details/140212378?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22140212378%22%2C%22source%22%3A%22Luoweijie42%22%7D)
   4. [luo的iOS](https://blog.csdn.net/Luoweijie42/article/details/140344444)
   3.xpath基础概念：[菜鸟教程](https://www.runoob.com/xpath/xpath-syntax.html)
   4.基础unittest教学视频：[哔哩哔哩](https://www.bilibili.com/video/BV1AT41167wv?p=5&vd_source=f1420afe1b941d0191a7f686b3a2f85c)

---