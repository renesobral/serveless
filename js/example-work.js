import React from 'react';

class ExampleWork extends React.Component {
  render(){
    return (
      <section className="section section--alignCentered section--description">
        {this.props.items.map( (item, idx) => {
            return (<ExampleWorkItem data={item} key={idx}/>);
          }
        )}

      </section>
    )
  }
}

class ExampleWorkItem extends React.Component {
  render(){
    let item = this.props.data;
    return (
    <div className="section__exampleWrapper">
      <div className="section__example">
        <img alt={item.image.description} className="section__exampleImage"
             src={item.image.src}/>
        {/* {item.image.comment} */}
        <dl className="color--cloud">
          <dt className="section__exampleTitle section__text--centered">
            {item.title}
          </dt>
          <dd></dd>
        </dl>
      </div>
    </div>
    )
  }
}

export default ExampleWork;
