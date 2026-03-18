import { getStakeholders } from '@/lib/store';
import Badge from '@/components/Badge';
import Link from 'next/link';
import DeleteButton from '@/components/DeleteButton';

export const dynamic = 'force-dynamic';

export default function StakeholdersPage() {
  const stakeholders = getStakeholders();

  return (
    <div className="space-y-5 max-w-5xl">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-slate-900">Stakeholders</h2>
          <p className="text-sm text-slate-500 mt-0.5">{stakeholders.length} total</p>
        </div>
        <Link
          href="/stakeholders/new"
          className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
        >
          + Add Stakeholder
        </Link>
      </div>

      {stakeholders.length === 0 ? (
        <div className="bg-white rounded-xl p-12 text-center shadow-sm border border-slate-200">
          <p className="text-slate-400 text-lg">No stakeholders yet.</p>
          <Link href="/stakeholders/new" className="mt-3 inline-block text-blue-600 hover:underline text-sm">
            Add your first stakeholder →
          </Link>
        </div>
      ) : (
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
          <table className="w-full text-sm">
            <thead className="bg-slate-50 border-b border-slate-200">
              <tr>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Name</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Organization</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Category</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Influence</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Interest</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Tags</th>
                <th className="px-4 py-3"></th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {stakeholders.map((s) => (
                <tr key={s.id} className="hover:bg-slate-50 transition-colors">
                  <td className="px-4 py-3">
                    <div className="flex items-center gap-2">
                      <div className="w-7 h-7 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-xs flex-shrink-0">
                        {s.name.charAt(0).toUpperCase()}
                      </div>
                      <div>
                        <Link href={`/stakeholders/${s.id}`} className="font-medium text-slate-800 hover:text-blue-600">
                          {s.name}
                        </Link>
                        <p className="text-xs text-slate-400">{s.role}</p>
                      </div>
                    </div>
                  </td>
                  <td className="px-4 py-3 text-slate-600">{s.organization}</td>
                  <td className="px-4 py-3"><Badge value={s.category} /></td>
                  <td className="px-4 py-3"><Badge value={s.influence} /></td>
                  <td className="px-4 py-3"><Badge value={s.interest} /></td>
                  <td className="px-4 py-3">
                    <div className="flex flex-wrap gap-1">
                      {s.tags.slice(0, 2).map((t) => (
                        <span key={t} className="bg-slate-100 text-slate-600 text-xs px-2 py-0.5 rounded">{t}</span>
                      ))}
                      {s.tags.length > 2 && <span className="text-xs text-slate-400">+{s.tags.length - 2}</span>}
                    </div>
                  </td>
                  <td className="px-4 py-3 text-right">
                    <div className="flex items-center gap-2 justify-end">
                      <Link href={`/stakeholders/${s.id}`} className="text-xs text-blue-600 hover:underline">Edit</Link>
                      <DeleteButton id={s.id} type="stakeholders" />
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
