#include <iostream>
#include <vector>
#include <fstream>
#include <istream>
#include <algorithm>

using namespace std;
vector<float> convertMV2C(vector<float>*refC,vector<float>*refMV,vector<float>*convert){
    vector<float>converted1;
    for(int i =0; i<convert->size();i++){
        float c = convert->at(i);
        int result;
        int j=0;
        while(c>refMV->at(j+1)){j++;}
        result = j;
        converted1.push_back(refC->at(result));
        cout<<refC->at(result)<<endl;

    }
    return converted1;
}

bool write2File(vector<float>*converted,string filename){


    ofstream myFile(filename);
    if(myFile.is_open()){
        for(int i = 0; i<converted->size();i++){
            myFile<<converted->at(i)<<endl;
        }

        myFile.clear();
        myFile.close();
        return true;
    }

    return false;
}

vector<float> readFromFile(string filename){

    //create new input filestream
    ifstream myFile2;
    bool read = true;
    string line;
    vector<float>convert;
    //filename of your reference data for the 24hr warmup experiment
    myFile2.open(filename,ios::in);

    if(!myFile2){read= false;}

    if(read){
        while (getline(myFile2,line)){

            convert.push_back(stof(line));
            //cout<<convert[idx]<<endl;

        }

        myFile2.close();
        myFile2.clear(myFile2.eofbit);
        myFile2.seekg(0, ios::beg);
        myFile2.close();

    }
    return convert;

}


int main() {
//arrays to hold the reference Data for converting mv->°C
vector<float> referenceC;
vector<float> referenceMV;

//bool to check if the file was opened or not
bool read = true;

//create the input file stream
ifstream myFile;
//this filename should be the reference csv file
myFile.open("tempsensorMV2C.csv", ios::in);

//check if file could be opened
if(!myFile){
    printf("failed to open file\n");
read = false;
}

//temp variables used to store the converted data from the filestream
float a,b;

string line;
int idx=0;
if(read) {

    while (!myFile.eof()) {
        //csv should be 2 columns so read each one in the representing vector
        myFile>>a;
        myFile>>b;
        referenceC.push_back(a);
        referenceMV.push_back(b);

        //printf("temp in C |temp in mv: %f|%f\n", referenceC[idx], referenceMV[idx]);
        idx++;
    }
//clear filreader and close it
    myFile.clear(myFile.eofbit);
    myFile.seekg(0, ios::beg);
    myFile.close();
    read=true;


}


//files to convert from  mV->°C
vector<float> convert;
vector<float> converted;
convert=readFromFile("kontroll.csv");
converted=convertMV2C(&referenceC,&referenceMV,&convert);
write2File(&converted,"controll1.csv");


//files to convert from  mV->°C
vector<float> convert1;
vector<float> converted1;
convert1=readFromFile("aufwaermen.csv");
converted1=convertMV2C(&referenceC,&referenceMV,&convert1);
write2File(&converted1,"messung1.csv");




    return 0;
}
