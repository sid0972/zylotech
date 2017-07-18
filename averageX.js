var mapFunction1 = function() {
emit(this.userID, this.X);
};

var reduceFunction1 = function(userID, X) {
total=0
for (var i=0;i<X.count();i++){
    total+=1
return Array.sum(X)/total;
}
};
db.transaction.mapReduce(
mapfunction1,
reduceFunction1,
{out:"mapreduce"}
)
