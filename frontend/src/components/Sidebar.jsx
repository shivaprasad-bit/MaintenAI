import {
  LayoutDashboard,
  Cpu,
  Bell,
  BarChart3,
  FileText,
  Wrench,
  Settings
} from "lucide-react";

const Item = ({ icon: Icon, text, active }) => (
  <div
    className={`flex items-center gap-3 p-3 rounded-xl cursor-pointer transition
      ${
        active
          ? "bg-blue-700 text-white"
          : "text-slate-400 hover:bg-slate-800 hover:text-white"
      }`}
  >
    <Icon size={20}/>
    <span>{text}</span>
  </div>
);

export default function Sidebar() {
  return (
    <div className="w-64 bg-[#071225] border-r border-cyan-500/20 p-5 flex flex-col">
      <h1 className="text-3xl font-bold text-cyan-400 mb-8">
        Mainten<span className="text-blue-500">AI</span>
      </h1>

      <div className="space-y-2">
        <Item icon={LayoutDashboard} text="Dashboard" active />
        <Item icon={Cpu} text="Machines"/>
        <Item icon={Bell} text="Alerts"/>
        <Item icon={BarChart3} text="Analytics"/>
        <Item icon={FileText} text="Reports"/>
        <Item icon={Wrench} text="Maintenance"/>
        <Item icon={Settings} text="Settings"/>
      </div>

      <div className="mt-auto">
        <div className="bg-slate-900 rounded-xl p-4 border border-green-500/30">
          <p className="text-xs text-slate-400">System Status</p>
          <p className="text-green-400 font-bold">ONLINE</p>
        </div>
      </div>
    </div>
  );
}