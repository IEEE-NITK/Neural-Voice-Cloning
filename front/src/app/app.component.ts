import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'front';
  serverData: JSON;
  but=0;
  text1 = 'No Result'
  text2 = 'No Result'
  text3 = 'No Result'
  text4 = 'No Result'
  color1='red'
  color2='red'
  color3='red'
  color4='red'
  baseurl = "http://127.0.0.1:5000/recognize/";

  constructor(private httpClient: HttpClient){
  //  console.log(js);
    console.log("asdf");

    //SineWaves(); 
  }

  get_products(id:number){
    this.baseurl += id;
    if( id == 1)
    {
      this.text1 = 'Wait'
    }
    if( id == 2)
    {
      this.text2 = 'Wait'
    }
    if( id == 3)
    {
      this.text3 = 'Wait'
    }
    if( id == 4)
    {
      this.text4 = 'Wait'
    }
    
    //console.log(this.baseurl);
    this.httpClient.get(this.baseurl).subscribe((res)=>{
      this.serverData = res as JSON;
        console.log(this.serverData['result']);
        
        if(id==1){
          if(this.serverData['result'])
          {
            console.log('true');
            this.color1='green';
            this.text1 = 'Successful';
          }else{
            console.log('false');
            this.color1='red';
            this.text1 = 'Record Again';
          }
          
        }
        if(id==2){
          if(this.serverData['result'])
          {
            console.log('true');
            this.color2='green';
            this.text2 = 'Successful';
          }else{
            console.log('false');
            this.color2='red';
            this.text2 = 'Record Again';
          }
        }
        if(id==3){
          if(this.serverData['result'])
          {
            console.log('true');
            this.color3='green';
            this.text3 = 'Successful';
          }else{
            console.log('false');
            this.color3='red';
            this.text3 = 'Record Again';
          }
        }
        if(id==4){
          if(this.serverData['result'])
          {
            console.log('true');
            this.color4='green';
            this.text4 = 'Successful';
          }else{
            console.log('false');
            this.color4='red';
            this.text4 = 'Record Again';
          }
        }
    });
 
    this.baseurl = "http://127.0.0.1:5000/recognize/";
}


}
