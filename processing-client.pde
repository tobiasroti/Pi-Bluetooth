import processing.net.*; 
Client myClient;
String COLOR_TYPE = "10"; 

void setup() {
myClient = new Client(this, "127.0.0.1", 5207);
}

void draw() {
    rvals = "0," + COLOR_TYPE + "," + r + "," +  g + "," + b + ",";
    gvals = "1," + COLOR_TYPE + "," + r + "," +  g + "," + b + ",";
    bvals = "2," + COLOR_TYPE + "," + r + "," +  g + "," + b + ",";
    
  if (dropTime == dropMax){
    myClient.write(rvals);
    myClient.write(gvals);
    //myClient.write(bvals);
}