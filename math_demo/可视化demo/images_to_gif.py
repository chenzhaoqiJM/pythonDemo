import imageio
import os


def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def main():
    images_path = './images'
    image_list = os.listdir(images_path)
    image_list = [os.path.join(images_path, image_name) for image_name in image_list]
    gif_name = os.path.join(images_path, 'my.gif')
    duration = 0.35
    create_gif(image_list, gif_name, duration)


if __name__ == '__main__':
    main()