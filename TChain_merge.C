void TChain_merge() {

        //Changeable pathways
        TString pathWay = "/w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/old";
        TString outWay = "/w/work3/home/zach/PairPol/FarmGeneratedEvents/";

        void *directory = gSystem->OpenDirectory(pathWay);
        void *Outdirectory = gSystem->OpenDirectory(outWay);

        //Sets up the varibles
        vector<TChain*> Chain;
        vector<Double_t> Pol;
        TString blank = "";
        TString filename; TString partial; TString Polstrip; TString move; TString fileName; TString Partial; TString polstrip; TString hadd;
        while((filename=(gSystem->GetDirEntry(directory)))){
                //If there is nothing inside the directory then stop
                if(filename == blank)
                        break;
                //If the directory does not contian '_1' then skip
                if(!filename.Contains("_1.root"))
                        continue;
                //So we can keep the actual directory names but strip them as well
                partial = filename;
                //Strips the file names
                partial.ReplaceAll("_1.root","*.root");
                Polstrip =TString(partial(partial.First("Pol")-14,14));
                Polstrip.ReplaceAll("_","").ReplaceAll("m", "");

                //Sets up the TChain
                TChain* chain = new TChain("SD",Polstrip);
                chain->Add(pathWay + "/" + partial);
                partial.ReplaceAll("*", "");
                cout << "Making trees for "<< partial <<" and found " << chain->GetListOfFiles()->GetEntries() << " '.root' files "<<endl;

                cout << partial << endl;
                //Merges the files
                chain->Merge(partial);

                Chain.push_back(chain);
                Pol.push_back(Polstrip.Atof());}



   cout<<"Found "<< Chain.size() <<" different polarizations" <<endl;

while((move=(gSystem->GetDirEntry(Outdirectory)))){
        if(move.Contains("Pol.root")){
                gSystem->Exec("mv 400*Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/");
                break;}}
/*for(Int_t i=0;i<pols.size();i++){

     cout<<pols[i]<<" "<<chains[i]->GetTitle()<<endl;

   }*/

        void *directory2= gSystem->OpenDirectory(pathWay);
        while((fileName=(gSystem->GetDirEntry(directory2)))){
                if(fileName == blank)
                        break;
                if(!fileName.Contains("_1.root"))
                        continue;
                        
                         Partial = fileName;
                Partial.ReplaceAll("_1.root","*.root");
                polstrip =TString(Partial(Partial.First("Pol")-14,14));
                polstrip.ReplaceAll("_","").ReplaceAll("m", "");


                TChain* chain2 = new TChain("GenParam",polstrip);
                chain2->Add(pathWay + "/" + Partial);
                Partial.ReplaceAll("*", "");
                cout << "Making trees for "<< Partial <<" and found " << chain2->GetListOfFiles()->GetEntries() << " '.root' files "<<endl;

                cout << Partial << endl;

                chain2->Merge(Partial);

                Chain.push_back(chain2);
                Pol.push_back(polstrip.Atof());}

while((hadd=(gSystem->GetDirEntry(Outdirectory)))){
        if(hadd == blank)
                break;
        if(!hadd.Contains(".root"))
                continue;

        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.125819975788Pol.roottot ./400MeV_0degrees_0mm_0.125819975788Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.125819975788Pol.root");
        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.45148837067Pol.roottot ./400MeV_0degrees_0mm_0.45148837067Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.45148837067Pol.root");
        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.470843382701Pol.roottot ./400MeV_0degrees_0mm_0.470843382701Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.470843382701Pol.root");
        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.635629120943Pol.roottot ./400MeV_0degrees_0mm_0.635629120943Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.635629120943Pol.root");
        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.809748334731Pol.roottot ./400MeV_0degrees_0mm_0.809748334731Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.809748334731Pol.root");
        gSystem->Exec("hadd 400MeV_0degrees_0mm_0.978981968771Pol.roottot ./400MeV_0degrees_0mm_0.978981968771Pol.root /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/400MeV_0degrees_0mm_0.978981968771Pol.root");
        break;
}

gSystem->Exec("mv 400MeV_0degrees_0mm_0.125819975788Pol.roottot 400MeV_0degrees_0mm_0.125819975788Pol.root");
gSystem->Exec("mv 400MeV_0degrees_0mm_0.45148837067Pol.roottot 400MeV_0degrees_0mm_0.45148837067Pol.root");
gSystem->Exec("mv 400MeV_0degrees_0mm_0.470843382701Pol.roottot 400MeV_0degrees_0mm_0.470843382701Pol.root");
gSystem->Exec("mv 400MeV_0degrees_0mm_0.635629120943Pol.roottot 400MeV_0degrees_0mm_0.635629120943Pol.root");
gSystem->Exec("mv 400MeV_0degrees_0mm_0.809748334731Pol.roottot 400MeV_0degrees_0mm_0.809748334731Pol.root");
gSystem->Exec("mv 400MeV_0degrees_0mm_0.978981968771Pol.roottot 400MeV_0degrees_0mm_0.978981968771Pol.root");
gSystem->Exec("mv 400* /w/work3/home/zach/PairPol/FarmGeneratedEvents/Randpoldeg_med/PolAsym_0/");


 return;}
