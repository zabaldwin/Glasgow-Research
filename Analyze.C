#include "TFile.h"
#include "TTree.h"
#include "TBrowser.h"
#include "TLorentzVector.h"
#include "TRandom.h"
#include "TClassTable.h"
#include "TROOT.h"
#include "TH1.h"
#include "TF1.h"
#include <iostream>
#include <vector>
#include <string>

void Analyze(){

        // Initializers 

        TString Poldeg[5] = {"0", "0.25", "0.5", "0.75", "1"};
        TString PolAsym[5] = {"0", "23", "45", "67", "90"};
        TString direct[5] = {"PolAsym_0/", "PolAsym_23/", "PolAsym_45/", "PolAsym_67/", "PolAsym_90/"};

        // Pathways 
        TString pathWay = "/w/work3/home/zach/PairPol/FarmGeneratedEvents/";
        TString outputPath = "/home/zach/geant4/pairPol/rootFiles/";


        // Sets up change-able input file
        TString changeFile =  "400MeV_" + PolAsym[4] + "degrees_0mm_" + Poldeg[0] + "Pol.root";

        // Sets up input trees
        TString input = pathWay + changeFile;
        cout << "This is the input: " << input << endl;

        TFile* iFile = new TFile(input, "read");
        TTree* iTree = (TTree*)iFile->Get("SD");

        // Set up constructors inside SD (or others if created)

        std::vector<Int_t> *hiti = 0;
        std::vector<Float_t> *hitx = 0; std::vector<Float_t> *hity = 0; std::vector<Float_t> *hitz = 0;
        std::vector<Float_t> *hite = 0; std::vector<Float_t> *hitt = 0;
        Double_t beamE;
        Int_t nhit;

        // Set up branches

        iTree->SetBranchAddress("hiti", &hiti);
        iTree->SetBranchAddress("nhit", &nhit);
        iTree->SetBranchAddress("hitx", &hitx); iTree->SetBranchAddress("hity", &hity);
        iTree->SetBranchAddress("hite", &hite);
        iTree->SetBranchAddress("beamE", &beamE);

        iTree->SetBranchStatus("hiti", 1);
        iTree->SetBranchStatus("nhit", 1);
        iTree->SetBranchStatus("hite", 1);
        iTree->SetBranchStatus("hitx", 1); iTree->SetBranchStatus("hity", 1);
        iTree->SetBranchStatus("beamE", 1);

        // Create output
        //string changeFile_append = changeFile.erase( changeFile.end()-5);
        changeFile.ReplaceAll(direct[4],"").ReplaceAll(".root","");
        
         //changeFile.ReplaceAll(".root", "");
        TString output = outputPath + changeFile + "_out.root";
        cout << "This is the output: " << output << endl;

        TFile* oFile = new TFile(output, "recreate");

        // Sets up variable bin widths

        const Int_t XBINS = 100; const Int_t YBINS = 100;

        // Setting up parameters

        TH2F* pix1_xy = new TH2F("Pix1-xy", "Pix1-xy", XBINS,-8, 8, YBINS, -8, 8);
        TH2F* pix2_xy = new TH2F("Pix2-xy", "Pix2-xy", XBINS, -8, 8, YBINS, -8, 8);

        TH2F* Sum_pix = new TH2F("Sum_pix1", "Sum_pix1", 2*XBINS, -16, 16, 2*YBINS, -16, 16);

        TH2F* Diff_pix = new TH2F("Diff_pix", "Diff_pix", 2*XBINS, -16, 16, 2*YBINS, -16, 16);

        TH1F* DiffinX = new TH1F("DiffinX", "DiffinX", 2*XBINS, -16, 16);
        TH1F* DiffinY = new TH1F("DiffinY", "DiffinY", 2*YBINS, -16, 16);

        TH2F* PhisetUp = new TH2F("PhisetUp", "PhisetUp", 2*XBINS, -16, 16, 2*YBINS, -16, 16);

        TH2F* Phi_pix = new TH2F("Phi_pix","Phi_pix", XBINS, 0, 4, YBINS, 0, 16);

        /*
        TH1F* Nhit = new TH1F("nhit", "nhit", XBINS, 0, 3);
        TH1F* hitI = new TH1F("hiti", "hiti", XBINS, 0, 3);
        TH1F* hitE = new TH1F("hite", "hiti", XBINS, 0, 0.5);
        TH1F* hitT = new TH1F("hitt", "hitt", XBINS, 0, 1.55);
        TH1F* hitX = new TH1F("hitx", "hitx", XBINS, -8, 8);
        TH1F* hitY = new TH1F("hity", "hity", XBINS, -8, 8);
        TH1F* hitZ = new TH1F("hitz", "hitz", XBINS, 0, 0.2);
        */
        Int_t count = 0; Int_t i = 0;
        Double_t totalDiffX = 0;
        Double_t totalDiffY = 0;

        // Adds a new branch to the existing tree
        Int_t entries = iTree->GetEntries();

        for (i; i<entries; i++){
                iTree->GetEntry(i);
                if(nhit != 2) continue;

                //Position Hits
                Float_t Pix1_xHit = hitx->at(hiti->at(0));
                Float_t Pix1_yHit = hity->at(hiti->at(0));

                Float_t Pix2_xHit = hitx->at(hiti->at(1));
                Float_t Pix2_yHit = hity->at(hiti->at(1));

                pix1_xy->Fill(Pix1_xHit,Pix2_yHit);
                pix2_xy->Fill(Pix2_xHit,Pix2_yHit);

                Int_t n_hit = nhit;
                 Int_t hit_i = hiti;
                Int_t hit_e = hite;
                Int_t hit_t = hitt;
                Int_t hit_x = hitx;
                Int_t hit_y = hity;
                Int_t hit_z = hitz;
*/

        //      Nhit->Fill(n_hit);
/*              hitI->Fill(hiti);
                hitE->Fill(hite);
                hitT->Fill(hitt);
                hitX->Fill(hitx);
                hitY->Fill(hity);
                hitZ->Fill(hitz);
*/
                Sum_pix->Fill((Pix1_xHit+Pix2_xHit),(Pix1_yHit-Pix2_yHit));

                Diff_pix->Fill((Pix1_xHit-Pix2_xHit),(Pix1_yHit-Pix2_yHit));

                DiffinX->Fill(Pix1_xHit-Pix2_xHit);
                DiffinY->Fill(Pix1_yHit-Pix2_yHit);

                totalDiffX += Pix1_xHit-Pix2_xHit;
                totalDiffY += Pix1_yHit-Pix2_yHit;
                count++;}



        Double_t AvgX = totalDiffX/count;
        Double_t AvgY = totalDiffY/count;

        cout<< AvgX << " " << AvgY << endl;

        for(i=0; i<entries; i++){
                iTree->GetEntry(i);
                if(nhit!=2) continue;

                Float_t Pix1_xHit = hitx->at(hiti->at(0));
                Float_t Pix2_xHit = hitx->at(hiti->at(1));

                Float_t Pix1_yHit = hity->at(hiti->at(0));
                Float_t Pix2_yHit = hity->at(hiti->at(1));

                TVector2 asymVec((Pix1_xHit-Pix2_xHit)-AvgX,(Pix1_yHit-Pix2_yHit)-AvgY);
                Phi_pix->Fill(asymVec.Phi(), asymVec.Mod());}

        //Nhit->Write(); //hitI->Write(); hitE->Write(); hitT->Write(); hitX->Write(); hitY->Write(); hitZ->Write();
        pix1_xy->Write(); pix2_xy->Write();
        Diff_pix->Write();
        Phi_pix->Write();
        Sum_pix->Write();
        DiffinX->Write(); DiffinY->Write();
return;}
