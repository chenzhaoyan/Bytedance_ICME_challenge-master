#/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse #argparse是python标准库里面用来处理命令行参数的库

def init_model_args():
  """
  Basic but important params for traning
  """
  parser = argparse.ArgumentParser()
  # training size
  # parser.add_argument() 向该对象中添加你要关注的命令行参数和选项
  parser.add_argument('--batch_size', type=int, default=40)
  parser.add_argument('--embedding_size', type=int, default=40)
  parser.add_argument('--num_epochs', type=int, default=200)

  # optimizer
  parser.add_argument('--optimizer', default='adam', choices=['adam', 'adagrad'])
  parser.add_argument('--lr', type=float, default=0.001)

  #necessary dir
  parser.add_argument('--save_model_dir', default='save_model')
  parser.add_argument('--training_path', required=True)
  parser.add_argument('--validation_path', required=True)

  #task
  parser.add_argument('--task', default="finish")

  #track
  parser.add_argument('--track', type=int, default=2)

  args = parser.parse_args()
  return args
