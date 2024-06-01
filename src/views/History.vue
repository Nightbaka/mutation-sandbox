<template>
    <div class="gen-alg-stats">
      <h2>Genetic Algorithm Run Statistics</h2>
      <table>
        <thead>
          <tr>
            <th>Run #</th>
            <th>Best Fitness</th>
            <th>Average Fitness</th>
            <th>Generations</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="run in runs" :key="run.id">
            <td>{{ run.id }}</td>
            <td>{{ run.bestFitness.toFixed(2) }}</td>
            <td>{{ run.avgFitness.toFixed(2) }}</td>
            <td>{{ run.generations }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'GeneticAlgorithmStats',
    data() {
      return {
        runs: [
          { id: 1, bestFitness: 0.98, avgFitness: 0.76, generations: 50 },
          { id: 2, bestFitness: 0.99, avgFitness: 0.78, generations: 55 },
          { id: 3, bestFitness: 0.97, avgFitness: 0.74, generations: 53 }
        ]
      };
    }
  }
  </script>
  
  <style scoped>
  .gen-alg-stats table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .gen-alg-stats th, .gen-alg-stats td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
  }
  
  .gen-alg-stats th {
    background-color: #f5f5f5;
  }
  
  .gen-alg-stats h2 {
    color: #333;
  }
  </style>
  