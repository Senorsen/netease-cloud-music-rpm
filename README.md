# 网易云音乐 rpm包
当前状态：Fedora 23 下安装后可以正常打开，测试中播放音乐等功能均可用。

## 安装
1. 安装 RPM Fusion 源，free 和 nonfree 都需要：http://rpmfusion.org/Configuration
2. 终端下执行：
```
sudo dnf install http://dl-http.senorsen.com/pub/package/linux/rpm/netease-cloud-music-0.9.0-1.x86_64.rpm
```
注意：该命令会下载一个30+MB的rpm，所以可能比较缓慢。
3. 在 Dash 中搜索 netease，即可看到网易云音乐的图标（与其他 Ubuntu、Debian 系统安装后使用方法无异）。

重要提醒：
安装后会安装我的 rpm repo 源，以供之后随源更新。如果不需要，可以手动删除，或者自己 clone 本仓库后修改打包脚本。

## 依赖
Fedora 23+ (低版本未测试), RPMFusion (free, nonfree)
 
## Copyright
网易云音乐是网易公司的注册商标，本repo与网易公司没有任何关系。

## Author
打包脚本： Senorsen <senorsen.zhang@gmail.com>

网易云音乐忠实用户。

