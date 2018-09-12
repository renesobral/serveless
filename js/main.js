import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const exampleData = [
  {
    'title': 'Work Example',
    'image': {
      "description" : "example screenshot of a project involving cats",
      "src" : "images/example1.png",
      "comment": "example screenshot of a project involving cats"
      }
    },
    {
      'title': 'Work Example2',
      'image': {
        "description" : "example screenshot of a project involving cats",
        "src" : "images/example2.png",
        "comment": "example screenshot of a project involving cats"
        }
      },
      {
        'title': 'Work Example3',
        'image': {
          "description" : "example screenshot of a project involving cats",
          "src" : "images/example3.png",
          "comment": `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
                      https://www.flickr.com/photos/37287295@N00/2540855181`
                    }
        }
    ]

ReactDOM.render(<ExampleWork items={exampleData}/>, document.getElementById("example-work"));
