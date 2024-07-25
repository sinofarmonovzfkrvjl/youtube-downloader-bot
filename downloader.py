import yt_dlp


def YouTubeDownloader(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/video.mp4',
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
        #     'preferredcodec': 'mp3',  # Convert audio to mp3
        #     'preferredquality': '192',  # Set the preferred quality (bitrate)
        # }],
        'format': 'bestvideo/best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=True)
    video_title = info_dict.get('title')
    video_id = info_dict.get('id')
    video_url = info_dict.get('webpage_url')
    uploader = info_dict.get('uploader')
    upload_date = info_dict.get('upload_date')
    duration = info_dict.get('duration')
    view_count = info_dict.get('view_count')
    like_count = info_dict.get('like_count')
    description = info_dict.get('description')
    tags = info_dict.get('tags')
    return {"title": video_title, "id": video_id, "url": video_url, "uploader": uploader, "upload_date": upload_date, "duration": duration, "view_count": view_count, "like_count": like_count, "description": description, "tags": tags}
