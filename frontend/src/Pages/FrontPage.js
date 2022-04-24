import React from 'react';
import '../CSS/FrontPage.css';
import { FrontPageLoc, Common} from '../Components/Localization.js';


FrontPageLoc.setLanguage('uk'); //Only changes this obj's lang TODO

function FrontPage() {
  return (
    <div className='Text-Container'>
        <p>{FrontPageLoc.Description}</p>
        
        <button className='Startbtn'>{FrontPageLoc.StartButton}</button>
    </div>
  );
}

export default FrontPage;
