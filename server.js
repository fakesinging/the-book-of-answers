import express from 'express'
import path from 'path'
import { fileURLToPath } from 'url';
const app = express()

import answers from "./book_of_answers.json" assert { type: "json"}

console.log(answers)

app.use(express.json())
app.use(express.urlencoded({extended: false}))

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

app.use(express.static(path.join(__dirname, 'public')))

app.get("/api", (req, res) => {
    res.status(200).json(answers)
})


app.listen(8080, () => console.log("Server is running on the port 8080"))