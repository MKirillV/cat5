import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

# Загрузка датасета
X = []
y = []
for i in range(1,8):
    file_path = f'dataset/{i}.mp3'
    audio, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(audio, sr=sr, n_mfcc=20)
    X.append(mfccs)
    y.append(1) # 1 - звук разбивающейся посуды

for i in range(1,8):
    file_path = f'dataset/{i}.mp3'
    audio, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(audio, sr=sr, n_mfcc=20)
    X.append(mfccs)
    y.append(0) # 0 - другой звук

# Разделение датасета на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Создание модели нейронной сети
model = Sequential()
model.add(Dense(128, input_shape=(20,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(np.array(X_train), np.array(y_train), epochs=50, batch_size=32, validation_data=(np.array(X_test), np.array(y_test)))

# Оценка качества модели на тестовой выборке
score = model.evaluate(np.array(X_test), np.array(y_test), batch_size=32)
print('Test accuracy:', score[1])

# Тестирование модели на новых звуках
file_path = 'test_sound.wav'
audio, sr = librosa.load(file_path)
mfccs = librosa.feature.mfcc(audio, sr=sr, n_mfcc=20)
result = model.predict(np.array([mfccs]))
if result[0][0] > 0.5:
    print('Звук разбивающейся посуды')
else:
    print('Другой звук')
