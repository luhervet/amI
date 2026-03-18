import { getStakeholders, getRelations, getActions } from '@/lib/store';
import Badge from '@/components/Badge';
import Link from 'next/link';

export const dynamic = 'force-dynamic';

function StatCard({ title, value, sub, href }: { title: string; value: number; sub: string; href: string }) {
  return (
    <Link href={href} className="bg-white rounded-xl p-5 shadow-sm border border-slate-200 hover:shadow-md transition-shadow">
      <p className="text-sm text-slate-500 font-medium">{title}</p>
      <p className="text-4xl font-bold mt-1 text-slate-900">{value}</p>
      <p className="text-xs text-slate-400 mt-1">{sub}</p>
    </Link>
  );
}

export default function Dashboard() {
  const stakeholders = getStakeholders();
  const relations = getRelations();
  const actions = getActions();

  const actionsByStatus = {
    pending: actions.filter((a) => a.status === 'pending').length,
    in_progress: actions.filter((a) => a.status === 'in_progress').length,
    completed: actions.filter((a) => a.status === 'completed').length,
    cancelled: actions.filter((a) => a.status === 'cancelled').length,
  };

  const highInfluence = stakeholders.filter((s) => s.influence === 'high').length;
  const criticalActions = actions.filter((a) => a.priority === 'critical' && a.status !== 'completed').length;

  const recentActions = [...actions]
    .sort((a, b) => new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime())
    .slice(0, 5);

  const recentStakeholders = [...stakeholders]
    .sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
    .slice(0, 5);

  return (
    <div className="space-y-6 max-w-6xl">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Dashboard</h2>
        <p className="text-slate-500 text-sm mt-1">Stakeholder landscape at a glance</p>
      </div>

      {/* KPI cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Stakeholders" value={stakeholders.length} sub={`${highInfluence} high influence`} href="/stakeholders" />
        <StatCard title="Relations" value={relations.length} sub="mapped connections" href="/relations" />
        <StatCard title="Actions" value={actions.length} sub={`${actionsByStatus.in_progress} in progress`} href="/actions" />
        <StatCard title="Critical Actions" value={criticalActions} sub="requiring immediate attention" href="/actions" />
      </div>

      {/* Breakdowns */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-xl p-5 shadow-sm border border-slate-200">
          <h3 className="font-semibold text-slate-800 mb-4">Action Status Breakdown</h3>
          <div className="space-y-3">
            {(Object.entries(actionsByStatus) as [string, number][]).map(([status, count]) => (
              <div key={status} className="flex items-center gap-3">
                <Badge value={status}>{status.replace('_', ' ')}</Badge>
                <div className="flex-1 bg-slate-100 rounded-full h-2">
                  <div
                    className="bg-blue-500 h-2 rounded-full transition-all"
                    style={{ width: actions.length ? `${(count / actions.length) * 100}%` : '0%' }}
                  />
                </div>
                <span className="text-sm font-medium text-slate-700 w-6 text-right">{count}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-xl p-5 shadow-sm border border-slate-200">
          <h3 className="font-semibold text-slate-800 mb-4">Stakeholder Categories</h3>
          {stakeholders.length === 0 ? (
            <p className="text-sm text-slate-400">No stakeholders yet.</p>
          ) : (
            <div className="space-y-2">
              {(['internal', 'external', 'partner', 'regulator', 'customer', 'supplier'] as const).map((cat) => {
                const count = stakeholders.filter((s) => s.category === cat).length;
                if (count === 0) return null;
                return (
                  <div key={cat} className="flex items-center gap-3">
                    <Badge value={cat} />
                    <div className="flex-1 bg-slate-100 rounded-full h-2">
                      <div
                        className="bg-purple-500 h-2 rounded-full"
                        style={{ width: `${(count / stakeholders.length) * 100}%` }}
                      />
                    </div>
                    <span className="text-sm font-medium text-slate-700 w-6 text-right">{count}</span>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>

      {/* Recent activity */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-xl p-5 shadow-sm border border-slate-200">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-slate-800">Recent Actions</h3>
            <Link href="/actions" className="text-xs text-blue-600 hover:underline">View all</Link>
          </div>
          {recentActions.length === 0 ? (
            <p className="text-sm text-slate-400">No actions yet.</p>
          ) : (
            <ul className="space-y-3">
              {recentActions.map((a) => (
                <li key={a.id} className="flex items-start gap-2">
                  <Badge value={a.status}>{a.status.replace('_', ' ')}</Badge>
                  <div className="min-w-0">
                    <p className="text-sm font-medium text-slate-800 truncate">{a.title}</p>
                    <p className="text-xs text-slate-400">{a.priority} priority</p>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="bg-white rounded-xl p-5 shadow-sm border border-slate-200">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-slate-800">Recently Added Stakeholders</h3>
            <Link href="/stakeholders" className="text-xs text-blue-600 hover:underline">View all</Link>
          </div>
          {recentStakeholders.length === 0 ? (
            <p className="text-sm text-slate-400">No stakeholders yet.</p>
          ) : (
            <ul className="space-y-3">
              {recentStakeholders.map((s) => (
                <li key={s.id} className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-sm flex-shrink-0">
                    {s.name.charAt(0).toUpperCase()}
                  </div>
                  <div className="min-w-0">
                    <p className="text-sm font-medium text-slate-800 truncate">{s.name}</p>
                    <p className="text-xs text-slate-400 truncate">{s.organization} · {s.role}</p>
                  </div>
                  <Badge value={s.influence} />
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
