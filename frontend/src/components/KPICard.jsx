export default function KPICard({
  title,
  value,
  unit,
  color="cyan"
}) {

  const colors={
    cyan:"text-cyan-400",
    green:"text-green-400",
    orange:"text-orange-400",
    purple:"text-purple-400"
  }

  return(
    <div className="bg-[#081527] border border-cyan-500/20 rounded-xl p-5 shadow-lg shadow-cyan-500/10">
      <p className="text-xs uppercase tracking-widest text-slate-400">
        {title}
      </p>

      <h1 className={`text-4xl font-bold mt-2 ${colors[color]}`}>
        {value}
        <span className="text-xl ml-1">{unit}</span>
      </h1>
    </div>
  )
}