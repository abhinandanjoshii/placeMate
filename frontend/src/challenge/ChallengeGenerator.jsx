import "react"
import {useState, useEffect} from "react"
import {MCQChallenge} from "./MCQChallenge.jsx"

export function ChallengeGenerator(){
    const [challenges, setChallenges] = useState()
    const [loading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)
    const [difficulty, setDifficulty] = useState("easy")
    const [quota, setQuota] = useState(null)

    const fetchQuota = async () => {
    }
    const generateChallenge = async () => {}
    const getNextResetTime = () => {}

    return <div className="challenge-container">
        <h2>Placement Challenge Generator</h2>

        <div className="quota-display">
            <p
    </div>
}