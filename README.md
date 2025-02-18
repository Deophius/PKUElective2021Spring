# PKUAutoElective 2021 Spring Version

*Final Update: 本项目作者并不是专业开发者，上传本项目的初衷仅是在 2021 年选课网站发生改动，而新的验证码识别模型开源之前，给大家提供一个 AutoElective 的过渡选项（现在它的使命也完成了）。2021 的春季学期将会是作者在 PKU 的最后一个学期（如果顺利毕业的话 233），因此今后这个项目将不会在再更新，希望大家理解。*

***
本项目基于 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective)，对 2021 春季学期的选课网站 API 改动进行了调整。并针对验证码系统的改动，将识别系统转为在线商用平台 [TT识图](http://www.ttshitu.com)（**打钱！打钱！**），目前识别准确度仍然略微堪忧。

## 安装

安装依赖项：

```
pip install -r requirements.txt
```

## 配置文件

### config.ini

参考 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective) 项目中的 `config.ini` 配置说明。

**WARNING：建议不要将刷新间隔 `refresh_interval` 调到过小，否则您的 ip 有可能被选课网短时间内封禁**

### apikey.json

**请首先将 apikey.sample.json 复制一份并改名为 apikey.json，并按照以下说明进行配置。**

该文件为 [TT识图](http://www.ttshitu.com) 平台的 API 密钥，在平台注册后，填入用户名与密码即可。由于该 API 需要收费，须在平台充值后方可使用（1 RMB 足够用到天荒地老了）。

```json
{
    "username": "xiaoming",
    "password": "xiaominghaoshuai" 
}
```

## 使用说明

### 基本用法

将项目 clone 至本地后，切换至项目根目录下并运行 `main.py` 即可。

```
cd PKUElective2021Spring
python3 elect_main.py
```

使用 `Ctrl + C` 输送 `KeyboardInterrupt`，可以终止程序运行。

在 Linux 环境也可以运行 `kill_elect.py`。这个脚本的主要目的是和 `at` 命令配合，实现在一段时间内运行。为了更好的支持 headless run，日志将输出到文件内，并且省略了大部分 debug 信息。

### 命令行参数

关于支持的命令行参数，参见 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective) 的使用说明。

### TT识图：无感学习模式

*本条目基于 [XiaoTian](https://github.com/xiaotianxt) 用户提出的 PR。*

关于无感学习的详细信息，可参见 [无感学习介绍页面](http://www.ttshitu.com/news/fcda89be991e4af8927c32527fb45b1e.html)。简而言之，无感模式可以达到更高的识别准确率（并且识别准确度会随着使用次数的增加而进一步提高），但使用费率也更高，且使用前期识别速率较低。

可以通过向 `apikey.json` 中传入额外参数 `enhanced_mode` 来控制无感学习模式是否开启（该参数缺省时默认不开启）：

```json
{
    "username": "xiaoming",
    "password": "xiaominghaoshuai",
    "enhanced_mode": true
}
```

**WARNING: 根据TT识图后台统计明细，无感学习模式前期单次识别耗时通常 > 3000ms，而普通模式下单次识别耗时通常 < 100ms。因此若您认为其他选课同学的手速足够快，请不要开启无感学习模式。**

### TT识图平台测试

配置好 `apikey.json` 后，在命令行运行 `python api_test.py` 以测试在线识图是否正常工作。

如正常运行，将输出

```
Captcha('vfg8') True
```


## 注意事项

* 作者可能无视 Issue 和 PR，如果您有更好的改进想法，请最好 clone 一份后自行改动！
* 请不要在公开场合（以及某匿名平台）传播此项目，以免造成不必要的麻烦！
* 刷课有风险 USE AT YOUR OWN RISK!
