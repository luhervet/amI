import { getRelations, getStakeholders } from '@/lib/store';
import Badge from '@/components/Badge';
import DeleteButton from '@/components/DeleteButton';
import RelationForm from '@/components/RelationForm';

export const dynamic = 'force-dynamic';

function StrengthDots({ value }: { value: number }) {
  return (
    <div className="flex gap-0.5">
      {[1, 2, 3, 4, 5].map((i) => (
        <div key={i} className={`w-2 h-2 rounded-full ${i <= value ? 'bg-blue-500' : 'bg-slate-200'}`} />
      ))}
    </div>
  );
}

export default function RelationsPage() {
  const relations = getRelations();
  const stakeholders = getStakeholders();

  function getName(id: string) {
    return stakeholders.find((s) => s.id === id)?.name || 'Unknown';
  }

  return (
    <div className="space-y-6 max-w-5xl">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Relations</h2>
        <p className="text-sm text-slate-500 mt-0.5">{relations.length} mapped connections</p>
      </div>

      <RelationForm stakeholders={stakeholders} />

      {relations.length === 0 ? (
        <div className="bg-white rounded-xl p-10 text-center shadow-sm border border-slate-200">
          <p className="text-slate-400">No relations mapped yet. Add one above.</p>
        </div>
      ) : (
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
          <table className="w-full text-sm">
            <thead className="bg-slate-50 border-b border-slate-200">
              <tr>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">From</th>
                <th className="px-2 py-3 text-slate-400">→</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">To</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Type</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Strength</th>
                <th className="text-left px-4 py-3 text-slate-600 font-medium">Description</th>
                <th className="px-4 py-3"></th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {relations.map((r) => (
                <tr key={r.id} className="hover:bg-slate-50">
                  <td className="px-4 py-3 font-medium text-slate-800">{getName(r.fromId)}</td>
                  <td className="px-2 py-3 text-slate-400 text-center">⇆</td>
                  <td className="px-4 py-3 font-medium text-slate-800">{getName(r.toId)}</td>
                  <td className="px-4 py-3"><Badge value={r.type} /></td>
                  <td className="px-4 py-3"><StrengthDots value={r.strength} /></td>
                  <td className="px-4 py-3 text-slate-500 text-xs max-w-xs truncate">{r.description || '—'}</td>
                  <td className="px-4 py-3 text-right">
                    <DeleteButton id={r.id} type="relations" />
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
