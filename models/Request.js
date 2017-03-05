/**
 * Created by ajijohn on 3/4/17.
 */

const mongoose = require('mongoose');

const requestSchema = new mongoose.Schema({
    customerEmail: { type: String,},
    handleRequest:String,
    inputFile: String,
    outputFile: String,
    status: String,
    originalname:String,
    size:String,
    customerName: String

}, { timestamps: true });


const Request = mongoose.model('Request', requestSchema);

module.exports = Request;
