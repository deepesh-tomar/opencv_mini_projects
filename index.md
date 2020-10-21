## Computer Vision And Shopping 

One of the most advancing development in computer science is happening in the area of computer vision and deep learning. This is an attempt of POC for the idea of making shopping in pandemic times more safe and convenient. As it was observed in time of COVID-19 pandemic that social distancing was adviced to everyone for the safety, but in 21st century life, it is not possible to completely isolate yourself, one needs to go for grocery shopping and has to stand in line for bill and exchange cash in order for purchasing. What if there was a way to avoid standing in close proximity with other people in line and buy product without use of paper or plastic money.

With the help of computer vision and deep learning algorithms there might be a way to overcome this problem. Suppose you go to a store for purchasing something but instead of traditional way, you just went into a store and pick up whatever you desire and walk out of store and get bill on your phone and pay online for that, with this you won't have to stand in line at store and for bill and you won't have to use cash or platic money for paying, you will pay digitally.
### Step-by-Step break down of process

When a person walks into a store he/she has to register themselves first through a online portal for verification (This is done only once when using the store for the first time). when that person enters a store with the help of computer vision one image of the customer is taken from a camera at enterance. Using deep learning algorithms such as VGG-16/VGG-19/RESNET50 person is indentified that person and his/her details are fetched from database such as name and preffered way of payment and assign his/her id to that person.
As that person shops in store and pick up goods, all those goods are added to his/hers virtual cart, every movement of the person is monitered using movement tracking in computer vision and when a good is picked it is detected by various sensors that are installed in the shelfs, one way to do that is use of weight sensor, if a good is picked, sensor will detect that change in weight and camera will indentify the person who is picking up good and that item will be added to their cart on database. If that person decided not to buy something anymore, as he/she places the good back into shelf, change in weight will be sensed by the sensors and item will be removed from the cart.
At the end when a person walks out of store, a e-bill be generated and amount will be deducted from their account and history of purchase will be updated in their database.


```
[image](https://user-images.githubusercontent.com/43062123/96736295-17eae380-13da-11eb-93c4-f6516cf81d5d.png)
```

