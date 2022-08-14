from capstone import Model
import torch
from torchvision import transforms
from PIL import Image
import numpy
import os
import io

model = Model()
model.load_state_dict(torch.load("./FirstModel", map_location='cpu'))


def get_combinations(shirts, pants, shoes):
    """

    :param : pants, shirts, shoes directory 에 저장한 사진을 읽는다.
    :return: _combination_list
    """
    _pants_list = []
    _shirts_list = []
    _shoes_list = []
    _combination_list = []    #상의, 하의, 신발 순서
    # 데이터 삽입
    _shirts_list = shirts
    _pants_list = pants
    _shoes_list = shoes
    for shirt in _shirts_list:
        for pant in _pants_list:
            for shoes in _shoes_list:
                _combination_list.append((shirt, pant, shoes))

    return _combination_list


def get_scores(in_tensor_u, in_tensor_p, in_tensor_s): #상의, 하의, 신발 순서
    """
    :param in_tensor_u: tensor type 으로 변환된 상의
    :param in_tensor_p: tensor type 으로 변환된 하의
    :param in_tensor_s: tensor type 으로 변환된 신발
    :return: score
    """
    score = model(in_tensor_u, in_tensor_p, in_tensor_s)
    return score


def image_transform(infile):
    """
    :param infile:
    :return:
    """
    input_transforms = [transforms.ToTensor(),
                        transforms.Resize((256, 256)),
                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                        ]
    my_transforms = transforms.Compose(input_transforms)
    image = Image.open(infile)
    timg = my_transforms(image)

    return timg

def sort_score(_re):

    return sorted(_re.items(), reverse=True) # .items() 튜플 리스트 리턴

def outfit_show(_re):
    for k, v in _re.items():
        Image.show(v)
