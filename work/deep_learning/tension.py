import tensorflow as tf

#Forward propagation
# input >weight>hidden layer 1(activation  funtion) > weights > hidden 2(Activation fun)
# > weights> output layers '''

#BAck propagation
#campare output to intended output >cost or loss function
#optimization function >minimize cost(Adamoptimizer,SGD<adaGrad)
  
mnist = input.read("ex3data1.mat",one_hot=True)