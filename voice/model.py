model.pymodel = Sequential()

model.add(ZeroPadding2D(padding=(1,1),input_shape = (X_train.shape[1],X_train.shape[2],1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (4, 7)))
model.add(ZeroPadding2D(padding=(1,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))

model.add(MaxPooling2D((3,3)))


for kernel in [np.power(2, i) for i in range(6,8)]:
    model.add(ZeroPadding2D(padding=(1,1)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Conv2D(kernel, (3, 3)))
    model.add(ZeroPadding2D(padding=(1,1)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Conv2D(kernel, (4, 7)))
    model.add(MaxPooling2D((3,3)))

model.add(ZeroPadding2D(padding=(1,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3, 3)))
model.add(ZeroPadding2D(padding=(1,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Conv2D(256, (3, 3)))

model.add(GlobalAveragePooling2D())

model.add(Dense(1024, activation='relu'))#64
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])