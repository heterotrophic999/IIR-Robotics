Team members:

Taratutin Wladimir

Pervyhin Danechka

Vitalii Shevtsov

Alyona Pozhidaeva


Для работы с собакой нужно установить:
- 1)untree_legged_sdk
- 2)unitree_ros
- 3)lcm
- 4)unitree_ros_to_real
Для этого можете воспльзоваться гайдом https://qiita.com/coder-penguin/items/6e1e66b36a2fd2fd20c6
Заменив catkin build на catkin make

Как установить голосовое управление:
1) Установка ROS пакетов:
  - 1. Выполните в папке catkin_ws/src git clone https://github.com/heterotrophic999/IIR-Robotics.git
  - 2. Выполните pip install для requirements.txt в папке alice scripts 
  - 3. Используйте catkin make для IIR_ros_Alisa и IIR_legged_real 
  - 4. В пакете unitree_legged_real поменяйте ros_udp high_udp(8090, "192.168.12.1", 8082, sizeof(HighCmd),
  - 5. В .bashrc добавьте 
     #export ROS_HOSTNAME=localhost
     export ROS_MASTER_URI=http://192.168.12.1:11311
     export ROS_IP=ваш ip в сети Unitree_GO...
2) Cоздание навыка для Алисы:
   - 1. Перейдите по ссылке. Примите условия и нажмите кнопку Войти. https://console.cloud.yandex.ru/
   - 2. Введите название нового облака и нажмите кнопку Создать.
   - 3. Создайте функцию в Yandex cloud:
     -  3.1. Откройте консоль управления.https://console.cloud.yandex.ru/
     -  3.2. Выберите Cloud Functions.
     -  3.3. Нажмите кнопку Создать функцию.
     -  3.4 Введите имя функции. Условия:
            длина — от 3 до 63 символов;
            может содержать строчные буквы латинского алфавита, цифры и дефисы;
            первый символ — буква, последний — не дефис.
            Например, my-first-function.
            
      - 3.5. Нажмите кнопку Создать.
      - 3.6. Если у вас нет платежного аккаунта, зарегистрируйте его.https://cloud.yandex.ru/docs/billing/quickstart/index
   - 4*.Если необходимо создайте базу данных как показано в примере https://github.com/avidale/demo-alice-translate-skill Уровень 2 работа с логами. После создания базы данных поменяйте ссылки в файлах parrot.py и  Alice_pub.py. Снова соберите пакет Ros_Alisa
   - 5. Создайте версию функции:
     -  5.1.  Создайте ZIP-архив из файлов в папке alice_scripts parrot-py.zip.
     -  5.2.  В консоли управления в каталоге, где хотите создать версию функции, откройте Cloud Functions. Выберите функцию.https://console.cloud.yandex.ru/
    -   5.3.  В разделе Последняя версия нажмите кнопку Создать в редакторе:
    
             - Задайте параметры версии:
             
              -  Среда выполнения: python37.
              
               - Таймаут, секунды: 3.
               
               - Память: 128 МБ.
               
               - Сервисный аккаунт: Не выбрано.
               
             - Подготовьте код функции:
             
              -  Способ: ZIP-архив.
              
               - Файл: parrot-py.zip.
               
               - Точка входа: parrot.handler.
               
             - Нажмите кнопку Создать версию.
             
   -  6. Укажите функцию в настройках навыка
     -   6.1 Перейдите в консоль разработчика навыка.https://dialogs.yandex.ru/developer/
      -  6.2 Создайте навык и перейдите на вкладку Настройки.
      -  6.3 В блоке Backend выберите вариант Функция в Yandex Cloud.
      -  6.4 Из выпадающего списка выберите функцию.
      -  6.5 Заполните обязательные поля в блоках Основные настройки и Публикация в каталоге.
      -  6.6 Версию диалога выберите приватную
      -  6.7 Внизу страницы нажмите кнопку Сохранить/
 3) Запустите Навык:
    1. roslaunch IIR_legged_real real.launch ctrl_level:=highlevel
    2. rosrun IIR_ros_Alisa Alisa_pub.py
    3. rosrun IIR_legged_real voice_commands

   
