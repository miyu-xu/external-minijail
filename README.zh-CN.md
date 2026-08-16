# Minijail（Android 固定版本）

[English](README.md) | 简体中文

Minijail 为 Linux 主机进程提供权限收敛和沙箱能力。BSCP 在 Linux/KVM 路径使用固定 Android
版本；macOS 与 Windows 的平台适配不能把 Minijail 不可用等同于“无需沙箱”，生产部署仍应
应用对应操作系统的最小权限控制。

修改 UID/GID、capability、namespace 或 seccomp 行为时必须进行安全评审，并验证失败路径为
关闭失败。
