 We need to create two applications one act as publisher, second one as consumer.

Publisher is responsible to broadcast packets of random NL range Geo Data at a random time inteval from 1.01 till 5 seconds.

Consumer is responsible to listen and process the events published by multiple publisher instances, aggregates to maximum of 1 second, if its later then one second, then it will be next record. 
Result is stored in a flat file. Due to possible network issues, a correction mechanism is implemented for previously saved aggregated records. The user is notified with a message on the console about the progress of the program.

A Sample program to start the publisher with n number of instances and start the consumer 


## Design and Implementation

https://miro.com/app/board/uXjVLl6J6ho=/?share_link_id=90043539765

The system at high level works as shown in the picture below.

Publishers uses randomized geo data within NL boundaries and publishes as series of events

Publishing channel can be Redis, Kafka, ZeroMQ or equavalent

Consumer continuously listens to the events and process it.

![high level design](image.png)

A simulater program is for the exercise purpose to launch the multiple instances of the publisher and to start the consumer

Publisher:
- Initialize sockets with a unique frequency
- Randomizers for timer, position and height
- Generate the packets
- Publish events continously on random time interval

Consumer
- Contiously listen to the events 
- Groups them into 1 second interview
- Averages poistions
- Stores results into a flat file
- Handles late packets by correcting previous results
- Notify

![system architecture](image-1.png)

Sample test executions:

Publishers triggered with 5 instances

![image](https://github.com/user-attachments/assets/ea454c3c-cef4-405c-925e-a6895498ee46)

Consumer

![image](https://github.com/user-attachments/assets/dd97deff-534d-4d29-a701-47a8d2fd16dc)


results are stored in a log file

![image](https://github.com/user-attachments/assets/edbfb6d4-104a-4691-b230-eeabe935d723)





