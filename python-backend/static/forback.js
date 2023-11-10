const func = async () => {
    const result = await fetch("http://smolatour.itatmisis.ru:8080/events/");
    const resultJSON = await result.json();

    
    console.log(resultJSON)
};

func();