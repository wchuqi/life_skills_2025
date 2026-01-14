import os
from PIL import Image
from PIL.ExifTags import TAGS
from rembg import remove


def process_image_with_metadata(input_path: str, output_path: str):
    """
    使用 rembg 移除背景，并保持原始图像的尺寸和元数据。
    """
    try:
        # --- 第1步：读取原始图像信息 ---
        print(f"正在读取原始图片: {input_path}")
        original_image = Image.open(input_path)
        original_size = original_image.size
        original_info = original_image.info  # 获取所有元数据

        print(f"原始尺寸: {original_size}")
        print(f"原始元数据: {original_info}")

        # --- 第2步：使用 rembg 移除背景 ---
        # rembg 处理后，图片可能会变成 RGBA 模式
        print("正在使用 rembg 移除背景...")
        with open(input_path, 'rb') as f:
            input_data = f.read()
        output_data = remove(input_data)
        no_bg_image = Image.open(io.BytesIO(output_data))

        # --- 第3步：调整尺寸并复制元数据 ---
        print(f"正在将抠图后的图片调整回原始尺寸 {original_size}...")
        # 使用 LANCZOS 是高质量的重采样滤镜
        resized_no_bg_image = no_bg_image.resize(original_size, Image.LANCZOS)

        # 将原始元数据复制到新图片上
        # 注意：如果抠图后是RGBA模式，而原图是RGB，某些元数据可能不兼容
        # 这里我们直接复制，Pillow会处理兼容性
        resized_no_bg_image.info = original_info

        # --- 第4步：保存最终图片 ---
        # 保存为 PNG 格式以保留透明度和元数据
        resized_no_bg_image.save(output_path, "PNG")

        print(f"✅ 处理完成！图片已保存至: {output_path}")
        print(f"最终图片尺寸: {resized_no_bg_image.size}")
        print(f"最终图片元数据: {resized_no_bg_image.info}")

    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_path}'")
    except Exception as e:
        print(f"❌ 处理过程中发生错误: {e}")


# --- 使用示例 ---
if __name__ == "__main__":
    import io  # 需要导入 io 模块来处理内存中的图像数据

    # 替换成你的图片路径
    input_file = "D:\\workspace\\code\\pingduoduo_images\\20251216\\原图.jpg"
    output_file = "D:\\workspace\\code\\pingduoduo_images\\20251216\\透明图.jpg"

    process_image_with_metadata(input_file, output_file)
