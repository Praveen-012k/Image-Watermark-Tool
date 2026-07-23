# Image Watermark Tool

A desktop GUI application built with Python (Tkinter) and Pillow that lets you add a text watermark to any image — no Photoshop required.

## Features

- Upload any image via a native file picker
- Live preview of the selected image inside the app
- Add custom watermark text through a simple input field
- Custom font, size, and color for the watermark
- Live preview of the watermarked result before saving
- Choose exactly where to save the final image, with sensible default filename and folder
- Error handling — prevents crashes if Preview/Save is clicked before an image is selected

## Technologies Used

- Python
- Tkinter (GUI)
- Pillow (image processing — `Image`, `ImageDraw`, `ImageFont`, `ImageTk`)

## How It Works

1. Click **Choose Img** to select an image from your computer — Pillow loads it, and a scaled-down preview appears in the app.
2. Type your watermark text into the text field.
3. Click **Preview** to see the watermark drawn onto a copy of the image, without affecting the original.
4. Click **Save** to draw the watermark onto the full-resolution image and export it to a location of your choice.

Internally, watermarking works by creating an `ImageDraw` object tied to a copy of the loaded image, then using `.text()` to render the watermark string onto it with a chosen font and fill color.

## Running the App
    python main.py

## Possible Future Improvements

- Adjustable watermark position (corners, center) via a dropdown
- Support for logo/image watermarks, not just text
- Adjustable opacity/transparency for the watermark
- Batch watermarking multiple images at once
