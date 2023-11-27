
import Guest from '../model/Guest'

//Class friends
export class Friends extends Guest
{
    constructor(name,dishes)
    {
        this.name = name;
        this.dishes = dishes;
        this.newFriend();
    }
}

//Function that generate users with class friends and put this objects in array listFriends
const NewFriend =(nameP = '',dishesP = '')=>
{
    const newFriend = new Friends(nameP, dishesP);
    ListFriends.push(newFriend)
}

NewFriend('Carlos',10);
NewFriend('Sofia',8);
NewFriend('Carlos',10);