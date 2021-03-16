#import the required libraries
import processing.serial.115200;
Serial mySerial;
Table table;
String filename;

void setup()
{
  #set mySerial to listen on COM port 10 at 115200 baud
  mySerial = new Serial(this, "COM10", 115200);
  
  table = new Table();
  table.addColumn("Date");
  table.addColumn("Time");
  table.addColumn("Heart Rate)");
  table.addColumn("O2");
  table.addColumn("Confidence");
}

void draw()
{
  #variables called each time a new data entry is received
  int d = day();
  int m = month();
  int y = year();
  int h = hour();
  int min = minute();
  int s = second();
  
  if(mySerial.available() > 0)
  {
    #set the value recieved as a String
    String value = mySerial.readString();
    #check to make sure there is a value
    if(value != null)
    {
      #add a new row for each value
      TableRow newRow = table.addRow();
     
     
      #place the new row and date under the "Date" column
      newRow.setString("Date", str(d) + "/" + str(m) + "/" + str(y));
      
      #place the new row and time under the "Time" column
      newRow.setString("Time", str(h) + ":" + str(min) + ":" + str(s));
      
      #place the new row and value under the "Heart Rate" column
      newRow.setString("Heart Rate", body.heartRate);
      
      #place the new row and value under the "O2" column
      newRow.setString("O2", body.oxygen);
      
      #place the new row and value under the "Confidence" column
      newRow.setString("Heart Rate", body.confidence);
    }
  }
}

void keyPressed()
{
  #save as a table in csv format(data/table - data folder name table)
  saveTable(table, "data-table.csv");
  filename = "data-" + year()+"-"+ nf(month(),2,0) +"-"+ nf(day(),2,0) + ".csv";
  exit();
}