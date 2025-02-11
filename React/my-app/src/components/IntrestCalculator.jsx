import React, {useState} from "react";

function IntrestCalculator(){
    const [principal, setPrincipal] = useState("")
    const [rate, setRate] = useState("")
    const [time, setTime] = useState('')
    const [type, setType] = useState('')
    const [result, setResult] = useState(null);
    const [incre, setIncre] = useState("");

    const calculateIntrest = () =>{
        let p = parseFloat(principal);
        let r = parseFloat(rate);
        let t = parseFloat(time);

        if (isNaN(p) ||isNaN(r) ||isNaN(t) || p<=0 || r<=0 || t<=0){
            setResult("Please enter valid input.")
            return;
        }

        let intrest = 0
        if (type === 'simple'){
            intrest = (p * t *r)/100;
        }else{
            intrest = p*(Math.pow(1+r/100,t)) -p;
        }
        setResult(`calculated ${type} intrest is: ${intrest.toFixed(2)}`);
    }

    return (
        <div style={styles.container}>
            <h2>Intrest Calculator</h2>
            <label>Principal (P):</label>
            <input 
            type="number"
            value={principal}
            onChange={(e)=>setPrincipal(e.target.value)}
            style={styles.input}
            placeholder="Enter Principal amount"
            />

            <label>Rate (R):</label>
            <input 
            type="number"
            value={rate}
            onChange={(e)=>setRate(e.target.value)}
            style={styles.input}
            placeholder="Enter rate"
            />

            <label>Time (T):</label>
            <input 
            type="number"
            value={time}
            onChange={(e)=>setTime(e.target.value)}
            style={styles.input}
            placeholder="Enter time"
            />

            <label>select intrest type</label>
            <select value={type} onChange={(e)=> setType(e.target.value)} style={styles.select}>
                <option value="simple">simple</option>
                <option value="compound">compund</option>
            </select>

            <button onClick={calculateIntrest} style={styles.button}>Calculate</button>
            {result && <div style={styles.result}><h3>{result}</h3></div> }
        </div>
    );
}

const styles = {
    container:{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: 20,
        border: "1px solid #ccc",
        borderRadius: 5,
        margin: 20,
    },
    input:{
        padding: 10,
        margin: 10,
        width: "60%",
    },
    select:{
        padding: 10,
        margin: 10,
        width: "60%",
    },
    button:{
        padding: 10,
        margin: 10,
        width: "60%",
        backgroundColor: "blue",
        color: "white",
        border: "none",
        borderRadius: 5,
        cursor: "pointer",
    },
    result:{
        padding: 10,
        margin: 10,
        width: "60%",
        border: "1px solid #ccc",
        borderRadius: 5,
    }

}

export default IntrestCalculator;