import cv2
import os

path_videos = './videos'
path_images = './images'
videos = os.listdir(path_videos)
videos.sort()
alphabetic_position_video = 1

video_capture = cv2.VideoCapture(f'{path_videos}/{videos[0]}')


def get_frame(seconds):
    video_capture.set(cv2.CAP_PROP_POS_MSEC, seconds * 1000)
    has_frames, image = video_capture.read()
    image = cv2.resize(image, (810, 1080))
    print(f'{path_videos}/{videos[alphabetic_position_video]}', end='')
    print(f' => {path_images}/{videos[alphabetic_position_video].split(".")[0]}/image_{count}.jpg')
    if has_frames:
        cv2.imwrite(f'{path_images}/{videos[alphabetic_position_video].split(".")[0]}/image_{count}.jpg', image)
    return has_frames


sec = 0
frame_rate = 0.5
count = 1
success = get_frame(sec)

while success:
    count += 1
    sec += frame_rate
    sec = round(sec, 2)
    success = get_frame(sec)
    if count == 100:
        break
