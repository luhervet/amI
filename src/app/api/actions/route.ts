import { NextRequest, NextResponse } from 'next/server';
import { getActions, createAction } from '@/lib/store';

export async function GET() {
  return NextResponse.json(getActions());
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const { title, description, stakeholderIds, status, priority, dueDate, owner, outcome, tags } = body;
  if (!title || !status || !priority) {
    return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
  }
  const action = createAction({
    title,
    description: description || '',
    stakeholderIds: stakeholderIds || [],
    status,
    priority,
    dueDate: dueDate || '',
    owner: owner || '',
    outcome: outcome || '',
    tags: tags || [],
  });
  return NextResponse.json(action, { status: 201 });
}
