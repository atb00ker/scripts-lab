import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  public input: string;

  constructor(private title: Title) { }

  ngOnInit(): void {
    this.title.setTitle('HelloWorld: About');
  }

}
