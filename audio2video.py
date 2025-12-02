import os
import subprocess

def add_cover_to_audio():
    # 检查封面图片是否存在
    cover_image = "cover.png"
    if not os.path.exists(cover_image):
        print(f"错误：封面图片 '{cover_image}' 不存在！")
        return

    # 支持的音频文件扩展名
    audio_extensions = ('.mp3', '.m4a')
    
    # 遍历当前文件夹中的所有文件
    for filename in os.listdir('.'):
        # 检查文件是否是音频文件
        if filename.lower().endswith(audio_extensions):
            # 构造输出文件名（将扩展名改为.mp4）
            output_filename = os.path.splitext(filename)[0] + ".mp4"
            
            # FFmpeg命令参数
            command = [
                'ffmpeg',
                '-loop', '1',                      # 循环封面图片
                '-i', cover_image,                # 输入封面图片
                '-i', filename,                   # 输入音频文件
                '-vf', 'scale=594:440',           # 视频尺寸
                '-c:v', 'libx264',                # 视频编码器
                '-c:a', 'aac',                    # 音频编码器
                '-shortest',                      # 以最短的输入流为准（即音频长度）
                '-pix_fmt', 'yuv420p',            # 像素格式
                '-y',                             # 覆盖输出文件（如果存在）
                output_filename                   # 输出文件名
            ]
            
            print(f"正在处理: {filename} -> {output_filename}")
            
            try:
                # 执行FFmpeg命令
                subprocess.run(command, check=True)
                print(f"成功生成: {output_filename}")
            except subprocess.CalledProcessError as e:
                print(f"处理 {filename} 时出错: {e}")
            except Exception as e:
                print(f"发生意外错误: {e}")

if __name__ == "__main__":
    add_cover_to_audio()
    print("所有音频文件处理完成！")

