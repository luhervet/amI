import { getActions, getStakeholders } from '@/lib/store';
import Badge from '@/components/Badge';
import DeleteButton from '@/components/DeleteButton';
import Link from 'next/link';

export const dynamic = 'force-dynamic';

export default function ActionsPage() {
  const actions = getActions();
  const stakeholders = getStakeholders();

  function getNames(ids: string[]) {
    return ids
      .map((id) => stakeholders.find((s) => s.id === id)?.name)
      .filter(Boolean)
      .join(', ');
  }

  const sorted = [...actions].sort((a, b) => {
    const pOrder = { critical: 0, high: 1, medium: 2, low: 3 };
    return (pOrder[a.priority] ?? 4) - (pOrder[b.priority] ?? 4);
  });

  return (
    <div className="space-y-5 max-w-6xl">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">Actions</h2>
          <p className="text-sm text-slate-500 mt-0.5">{actions.length} tactical actions</p>
        </div>
        <Link
          href="/actions/new"
          className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
        >
          + New Action
        </Link>
      </div>

      {actions.length === 0 ? (
        <div className="bg-white rounded-xl p-12 text-center shadow-sm border border-slate-200">
          <p className="text-slate-400 text-lg">No actions yet.</p>
          <Link href="/actions/new" className="mt-3 inline-block text-blue-600 hover:underline text-sm">
            Create your first action →
          </Link>
        </div>
      ) : (
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
          <table className="w-full text-sm">
            <thead className="bg-slate-50 border-b border-slate-200">
              <tr>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Title</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Status</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Priority</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Due Date</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Owner</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Stakeholders</th>
                <th className="px-4 py-3"></th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {sorted.map((a) => (
                <tr key={a.id} className="hover:bg-slate-50 transition-colors">
                  <td className="px-4 py-3">
                    <Link href={`/actions/${a.id}`} className="font-medium text-slate-800 hover:text-blue-600">
                      {a.title}
                    </Link>
                    {a.description && <p className="text-xs text-slate-400 truncate max-w-xs">{a.description}</p>}
                  </td>
                  <td className="px-4 py-3"><Badge value={a.status}>{a.status.replace('_', ' ')}</Badge></td>
                  <td className="px-4 py-3"><Badge value={a.priority} /></td>
                  <td className="px-4 py-3 text-slate-500">{a.dueDate || '—'}</td>
                  <td className="px-4 py-3 text-slate-600">{a.owner || '—'}</td>
                  <td className="px-4 py-3 text-slate-500 text-xs max-w-xs truncate">
                    {a.stakeholderIds.length ? getNames(a.stakeholderIds) : '—'}
                  </td>
                  <td className="px-4 py-3 text-right">
                    <div className="flex items-center gap-2 justify-end">
                      <Link href={`/actions/${a.id}`} className="text-xs text-blue-600 hover:underline">Edit</Link>
                      <DeleteButton id={a.id} type="actions" />
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
