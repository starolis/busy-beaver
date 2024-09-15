'use client'

import { useState, useEffect } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Progress } from "@/components/ui/progress"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { startSimulation, getResults, connectWebSocket } from '../api/simulationApi'

type SimulationResult = {
  maxOnes: number
  maxSteps: number
  bestProductivityMachine: string
  bestStepMachine: string
  haltingMachines: number
  nonHaltingMachines: number
}

export default function BusyBeaverSimulator() {
  const [numStates, setNumStates] = useState(3)
  const [maxSteps, setMaxSteps] = useState(10000)
  const [isSimulating, setIsSimulating] = useState(false)
  const [progress, setProgress] = useState(0)
  const [result, setResult] = useState<SimulationResult | null>(null)

  useEffect(() => {
    const ws = connectWebSocket((data) => {
      if (data.progress) {
        setProgress(data.progress);
      }
    });

    return () => {
      ws.close();
    };
  }, []);

  const startSimulationHandler = async () => {
    setIsSimulating(true)
    setProgress(0)
    setResult(null)
    
    try {
      await startSimulation(numStates, maxSteps);
      // Poll for results
      const pollInterval = setInterval(async () => {
        const results = await getResults();
        if (results.message !== "Results not available yet") {
          clearInterval(pollInterval);
          setResult(results);
          setIsSimulating(false);
        }
      }, 1000);
    } catch (error) {
      console.error("Error starting simulation:", error);
      setIsSimulating(false);
    }
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Busy Beaver Turing Machine Simulator</h1>
      <Card>
        <CardHeader>
          <CardTitle>Simulation Configuration</CardTitle>
          <CardDescription>Set the parameters for the Busy Beaver simulation</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label htmlFor="numStates">Number of States</Label>
              <Input
                id="numStates"
                type="number"
                value={numStates}
                onChange={(e) => setNumStates(parseInt(e.target.value))}
                min={2}
                max={5}
              />
            </div>
            <div>
              <Label htmlFor="maxSteps">Max Steps</Label>
              <Input
                id="maxSteps"
                type="number"
                value={maxSteps}
                onChange={(e) => setMaxSteps(parseInt(e.target.value))}
                min={1000}
                max={1000000}
              />
            </div>
          </div>
        </CardContent>
        <CardFooter>
          <Button onClick={startSimulationHandler} disabled={isSimulating}>
            {isSimulating ? 'Simulating...' : 'Start Simulation'}
          </Button>
        </CardFooter>
      </Card>

      {isSimulating && (
        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Simulation Progress</CardTitle>
          </CardHeader>
          <CardContent>
            <Progress value={progress} className="w-full" />
          </CardContent>
        </Card>
      )}

      {result && (
        <Card className="mt-6">
          <CardHeader>
            <CardTitle>Simulation Results</CardTitle>
          </CardHeader>
          <CardContent>
            <Tabs defaultValue="productivity">
              <TabsList>
                <TabsTrigger value="productivity">Productivity Busy Beaver</TabsTrigger>
                <TabsTrigger value="steps">Longest Halting Busy Beaver</TabsTrigger>
                <TabsTrigger value="stats">Statistics</TabsTrigger>
              </TabsList>
              <TabsContent value="productivity">
                <p>Max 1's produced: {result.maxOnes}</p>
                <p>Best Productivity Machine:</p>
                <pre className="bg-gray-100 p-2 rounded mt-2">{result.bestProductivityMachine}</pre>
              </TabsContent>
              <TabsContent value="steps">
                <p>Max steps before halting: {result.maxSteps}</p>
                <p>Longest Halting Machine:</p>
                <pre className="bg-gray-100 p-2 rounded mt-2">{result.bestStepMachine}</pre>
              </TabsContent>
              <TabsContent value="stats">
                <p>Total Halting Machines: {result.haltingMachines}</p>
                <p>Total Non-Halting Machines: {result.nonHaltingMachines}</p>
              </TabsContent>
            </Tabs>
          </CardContent>
        </Card>
      )}
    </div>
  )
}