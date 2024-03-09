const express = require('express');
const router = express.Router();
const { MongoClient, ObjectId } = require('mongodb');

// MongoDB connection URI
const mongoURI = 'mongodb://localhost:27017';
const dbName = 'your_database_name'; 
const collectionName = 'questions';


router.post('/', async (req, res) => {
  try {
    const client = new MongoClient(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    await client.connect();

    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const { question, answer } = req.body;

    const result = await collection.insertOne({ question, answer });

    client.close();

    res.status(201).json({ message: 'Question added successfully', question: result.ops[0] });
  } catch (error) {
    console.error('Error adding question:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

router.put('/:id', async (req, res) => {
  try {
    const client = new MongoClient(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
    await client.connect();

    const db = client.db(dbName);
    const collection = db.collection(collectionName);

    const { id } = req.params;
    const { answer } = req.body;

    const result = await collection.updateOne({ _id: ObjectId(id) }, { $set: { answer } });

    if (result.modifiedCount === 0) {
      client.close();
      return res.status(404).json({ message: 'Question not found' });
    }

    client.close();

    res.status(200).json({ message: 'Question updated successfully' });
  } catch (error) {
    console.error('Error updating question:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

module.exports = router;
