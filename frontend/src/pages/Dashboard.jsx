import { useEffect, useState } from "react";

import api from "../services/api";

import Sidebar from "../components/Sidebar";
import KPICard from "../components/KPICard";
import TemperatureChart from "../components/TemperatureChart";

export default function Dashboard(){

  const[sensor,setSensor]=useState(null);
  const[history,setHistory]=useState([]);

  async function load(){

    const sensorRes=await api.get("/machines/MTR-001/sensor");

    const historyRes=await api.get("/machines/MTR-001/history");

    setSensor(sensorRes.data);

    setHistory(historyRes.data.history);

  }

  useEffect(()=>{

    load();

    const timer=setInterval(load,2000);

    return()=>clearInterval(timer);

  },[]);

  if(!sensor){

    return(
      <div className="h-screen bg-[#050B18] text-white flex items-center justify-center">
        Connecting...
      </div>
    )
  }

  return(

    <div className="flex h-screen bg-[#050B18] text-white">

      <Sidebar/>

      <div className="flex-1 overflow-auto p-6">

        <div className="flex items-center justify-between mb-6">

          <div>
            <h1 className="text-4xl font-bold text-cyan-300">
              Factory Command Center
            </h1>

            <p className="text-slate-400">
              Real-time Industrial Monitoring
            </p>
          </div>

          <div className="bg-green-500/20 border border-green-400 px-4 py-2 rounded-full text-green-400 font-semibold">
            ● {sensor.status}
          </div>

        </div>

        <div className="grid grid-cols-5 gap-4 mb-6">

          <KPICard
            title="Health"
            value={sensor.health}
            unit="%"
            color="green"
          />

          <KPICard
            title="Temperature"
            value={sensor.temperature}
            unit="°C"
            color="orange"
          />

          <KPICard
            title="RPM"
            value={sensor.rpm}
            color="cyan"
          />

          <KPICard
            title="Voltage"
            value={sensor.voltage}
            unit="V"
            color="purple"
          />

          <KPICard
            title="Failure Risk"
            value={sensor.failure_probability}
            unit="%"
            color="orange"
          />

        </div>

        <div className="grid grid-cols-3 gap-6">

          <div className="col-span-2">

            <TemperatureChart data={history}/>

          </div>

          <div className="bg-[#081527] border border-cyan-500/20 rounded-2xl p-5 shadow-lg shadow-cyan-500/10">

            <h2 className="text-lg font-semibold text-cyan-300 mb-4">
              AI Maintenance
            </h2>

            <div className="space-y-5">

              <div>

                <p className="text-slate-400 text-sm">Recommendation</p>

                <p className="text-white">{sensor.recommendation}</p>

              </div>

              <div>

                <p className="text-slate-400 text-sm">Failure Probability</p>

                <h1 className="text-4xl text-orange-400 font-bold">
                  {sensor.failure_probability}%
                </h1>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>

  )

}