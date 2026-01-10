from cmd_encap import CMD

returncode, stdout, stderr = CMD.run_bat("cmd.bat")
print(f"BAT返回码: {returncode}", "\n")
print(f"BAT输出:{stdout}")

