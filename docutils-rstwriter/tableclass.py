# Copyright 2020 Tomas Brabec
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Cell(object):

    def __init__(self):
        self.morecols = 0
        self.morerows = 0
        self.lesscols = 0
        self.lessrows = 0

    def get_text(self):
        return None

    def get_colwidth(self):
        t = self.get_text()
        if t == None:
            lines = []
        else:
            lines = t.splitlines()
        w = 0
        for l in lines:
            w = max(w,len(l))
        return w

    def get_lineheight(self):
        t = self.get_text()
        if t == None:
            return 0
        else:
            return len(t.splitlines())

    def get_line(self, index):
        t = self.get_text()
        if t == None:
            lines = []
        else:
            lines = t.splitlines()
        if index >= len(lines):
            return None
        else:
            return lines[index]

class EmptyCell(Cell):
    pass

class MultiCell(Cell):

    def __init__(self, text=None, morecols=0, morerows=0):
        super(MultiCell,self).__init__()
        self.morecols = morecols
        self.morerows = morerows
        self.text = text

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text


class SimpleCell(MultiCell):

    def __init__(self, text=None):
        super(SimpleCell,self).__init__(text,0,0)


class RefCell(Cell):

    def __init__(self, ref, morecols, lesscols, morerows, lessrows, prev_row):
        super(RefCell,self).__init__()
        self.morecols = morecols
        self.morerows = morerows
        self.lesscols = lesscols
        self.lessrows = lessrows
        self.ref = ref
        self.prev_row = prev_row

    def get_text(self):
        return self.ref.get_text()

    def get_lineheight(self):
        return self.ref.get_lineheight()

    def get_line(self, index):
        return self.ref.get_line(index)

    def get_colwidth(self):
        return self.ref.get_colwidth()


class rowclass(object):

    def __init__(self, colcount=0, isheader=0):
        self.cells = []
        if colcount > 0:
            for i in range(0,colcount): self.cells.append(None)
        self.isheader = isheader
        self.lastcell = 0
        pass

    def add_cell(self, cell=None):
        if cell == None:
            self.cells.append(None)
        elif isinstance(cell, cellclass):
            self.cells.append(cell)

    def get_cell(self, col):
        if col < len(self.cells):
            return self.cells[col]
        else:
            return None

    def get_rowheight(self, ignore_rowspan=0):
        h = 0; # row height
        i = 0; # column index
        for c in self.cells:
            if c.lesscols > 0:
                # This shall be a RefCell with the same height as the one
                # it is referencing. Hence we may skip it.
                assert isinstance(c, RefCell)
                assert i >= c.lesscols
            elif c.morerows==0:
                # Skip cells that span beyond this row. Only if this is
                # a row where the cell's rowspan ends we count it into
                # the row height.
                if c.lessrows == 0:
                    h = max(h, c.get_lineheight())
                elif not ignore_rowspan:
                    assert isinstance(c, RefCell)
                    l = c.get_lineheight()
                    cc = c
                    while cc.lessrows > 0:
                        # Reduce line height by the height of the previous row
                        # (+1 for that row's border line).
                        r = cc.prev_row
                        l -= r.get_rowheight(ignore_rowspan) - 1
                        cc = r.get_cell(i)
                        assert cc != None
                    assert not isinstance(cc, RefCell)
                    h = max(h,l)
            i += 1
        return h

    def format(self):
        t = ''
        for i in range(0, self.get_lineheight()):
            l = ''
            for c in self.cells:
                if len(l) > 0: l += ','
                l += c.get_line(i)
            t += l + '\n'
        return t


class tableclass(object):

    def __init__(self):
        self.colwidths = []
        self.rows = []
        self.lastrow = 0

    def get_colcount(self):
        colcount = 0
        for r in self.rows:
            colcount = max(colcount, len(r.cells))
        return colcount

    def get_colwidths(self, colcount):
        colcount = max(0,colcount)
        colwidths = [0] * colcount
        for i in range(0, min(colcount,len(self.colwidths))):
            colwidths[i] = self.colwidths[i]

        # increase colwidths so that each cell in a column will fit in the width
        for i in range(0,colcount):
            colcells = []
            for r in self.rows:
                c = r.get_cell(i)
                if c != None: colcells.append(c)

            w = colwidths[i]
            for c in colcells:
                if c.lessrows > 0:
                    # This shall be a RefCell with the same width as the one
                    # it is referencing. Hence we may skip it.
                    assert isinstance(c, RefCell)
                elif c.morecols==0:
                    # Skip cells that span beyond this column. Only if this is
                    # a column where the cell's colspan ends we count it into
                    # the column width.
                    if c.lesscols == 0:
                        w = max(w, c.get_colwidth())
                    else:
                        assert isinstance(c, RefCell)
                        assert i >= c.lesscols
                        cw = c.get_colwidth()
                        # Reduce column width by widths of preceding columns
                        # being spanned (+3 for those columns's begin/end
                        # space and border line).
                        cw -= sum(colwidths[i-c.lesscols:i]) + 3*c.lesscols
                        w = max(w,cw)
            colwidths[i] = w

        return colwidths

    def get_rowheights(self, rowcount):
        rowcount = max(0,rowcount)
        rowheights = [0] * rowcount

        for i in range(0,rowcount):
            r = self.rows[i]
            h = rowheights[i]
            j = 0
            for c in r.cells:
                if c.lesscols > 0:
                    # This shall be a RefCell with the same height as the one
                    # it is referencing. Hence we may skip it.
                    assert isinstance(c, RefCell)
                    assert j >= c.lesscols
                elif c.morerows==0:
                    # Skip cells that span beyond this row. Only if this is
                    # a row where the cell's rowspan ends we count it into
                    # the row height.
                    if c.lessrows == 0:
                        h = max(h, c.get_lineheight())
                    else:
                        assert isinstance(c, RefCell)
                        assert i >= c.lessrows
                        # Reduce line height by the height of all previous rows
                        # that the cell spans.
                        l = c.get_lineheight()
                        l -= sum(rowheights[i-c.lessrows:i]) + c.lessrows
                        h = max(h,l)
                j += 1
            rowheights[i] = h

        return rowheights

    def add_row(self, cells):
        cellcount = 0
        rowcount = 1
        for c in cells:
            cellcount += 1 + c.morecols
            rowcount = max(rowcount, 1+c.morerows)

        colcount = self.get_colcount()
        if self.lastrow < len(self.rows):
            # increase `cellcount` by the number of cells already
            # reserved in the row (typically due to multi-row cells
            # in the preceding row)
            for c in self.rows[self.lastrow].cells:
                if isinstance(c,RefCell): cellcount += 1

        colcount = max(colcount, cellcount)

        for i in range(0, rowcount-(len(self.rows)-self.lastrow)):
            row = rowclass()
            row.cells = [None] * colcount
            self.rows.append(row)

        rows = self.rows[self.lastrow:self.lastrow+rowcount]
        col = 0
        for c in cells:
            while col < colcount and \
                    col < len(rows[0].cells) and \
                    rows[0].cells[col] != None:
                col += 1

            # add missing cells (if any) for all rows
            for r in rows:
                diff = col + c.morecols - len(r.cells) + 1
                if diff > 0:
                    r.cells.append([None] * diff)

            # replace empty cell with the new one
            rows[0].cells[col] = c;
            rowspan = c.morerows+1
            colspan = c.morecols+1
            for j in range(1, rowspan):
                rows[j].cells[col] = RefCell(ref=c, morerows=rowspan-j-1,
                        lessrows=j, morecols=c.morecols, lesscols=0,
                        prev_row=rows[j-1])
            for i in range(1, colspan):
                for j in range(0, rowspan):
                    prev_row = None
                    if j > 0: prev_row = rows[j-1]
                    rows[j].cells[col+i] = RefCell(ref=c, morerows=rowspan-j-1,
                            lessrows=j, morecols=colspan-i-1, lesscols=i,
                            prev_row=prev_row)

        self.lastrow += 1

    def get_cell(self, row, col):
        if row >= len(self.rows):
            return None
        return self.rows[row].get_cell(col)

    def format(self):
        colcount = self.get_colcount()
        colwidths = self.get_colwidths( colcount )
        rowcount = len(self.rows)
        rowheights = self.get_rowheights( rowcount )

        t = ''
        trule_marks = None
        brule_marks = None
        rule = None
        for ri in range(0, rowcount):
            r = self.rows[ri]

            i = 0
            ctexts = []
            cwidths = []
            cells = []
            for c in r.cells:
                if c == None:
                    ctexts.append( None )
                    cwidths.append( colwidths[i] )
                    cells.append(c)
                elif c.lesscols == 0:
                    #TODO try:
                    #TODO     assert isinstance(c, MultiCell)
                    #TODO except AssertionError:
                    #TODO     print c.__class__.__name__
                    #TODO     raise
                    ctext = c.get_text().splitlines()
                    if c.lessrows > 0:
                        # remove lines that will span preceding rows
                        h = sum(rowheights[ri-c.lessrows:ri]) + c.lessrows
                        ctext = ctext[h:]
                    ctexts.append( ctext )
                    cw = sum(colwidths[i:i+1+c.morecols]) + 3*c.morecols
                    cwidths.append(cw)
                    cells.append(c)
                i += 1

            brule_marks = {0}
            m = 0
            for cw in cwidths:
                m += cw + 3
                brule_marks.add(m)

            if trule_marks == None:
                trule_marks = brule_marks

            # create horizontal rule
            if rule == None:
                # creating a brand new rule
                # (hence need only top rule marks)
                rule = '-' * (sum(cwidths) + 3*len(cwidths) + 1)
                rule = list(rule)
                for m in trule_marks:
                    rule[m] = '+'
                rule = ''.join(rule)
            else:
                # reusing the rule from the previous iteration
                # (hence need to add bottom rule marks)
#TODO                print rule
                rule = list(rule)
                for m in brule_marks:
                    try:
                        assert rule[m] in ('-', '+', '=', '|')
                    except AssertionError:
                        print 'rule[' + str(m) + ']=\'' + rule[m] + '\''
                        raise
                    if rule[m] != '|':
                        rule[m] = '+'
                rule = ''.join(rule)

            t += rule + '\n'
#TODO            print rule

            # add text lines (up to row's height)
            for l in range(0, rowheights[ri]):
                line = ''
                for i in range(0, len(ctexts)):
                    cw = cwidths[i]
                    fmt = '{0: <' + str(cw) + '}'
                    if len(line) == 0: line += '|'

                    if ctexts[i] == None or len(ctexts[i]) <= l:
                        line += ' ' * (1+cw)
                    else:
                        line += ' ' + fmt.format(ctexts[i][l])
                    line += ' |'
                t += line + '\n'
#TODO                print line

            # update variables for next iteration
            trule_marks = brule_marks

            # prepare horizontal rule for the next iteration
            # (we need to treat row spanning cells right)
            rule = ''
            l = rowheights[ri]
            for i in range(0, len(ctexts)):
                cw = cwidths[i]
                fmt = '{0: <' + str(cw) + '}'

                # add rule segments
                if ctexts[i] == None or cells[i].morerows == 0:
                    rule_char = '-'
                    if r.isheader: rule_char = '='
                    rule += '+' + rule_char * (cw+2)
                else:
#TODO                    if len(rule) == 0: rule += '|'
                    if i==0 or cells[i-1].morerows > 0:
                        rule += '|'
                    else:
                        rule += '+'
                    if len(ctexts[i]) > l:
                        rule += ' ' + fmt.format(ctexts[i][l]) + ' '
                    else:
                        rule += ' ' * (2 + cwidths[i])

                # at the end of the rule
                if i == len(ctexts)-1:
                    if ctexts[i] == None or cells[i].morerows == 0:
                        rule += '+'
                    else:
                        rule += '|'
        if rule != None:
            t += rule
        return t


if __name__ == '__main__':
    t = tableclass()

    cells = []
    cells.append( SimpleCell('1.1') )
    cells.append( SimpleCell('1.2') )
    cells.append( SimpleCell('1.3') )
    cells.append( SimpleCell('1.4') )
    cells.append( SimpleCell('1.5') )
    t.add_row(cells)

    cells = []
    cells.append( SimpleCell('2.1') )
    cells.append( SimpleCell('2.2') )
    cells.append( SimpleCell('2.3') )
    cells.append( SimpleCell('2.4') )
    cells.append( SimpleCell('2.5') )
    t.add_row(cells)

    cells = []
    cells.append( SimpleCell('3.1') )
    cells.append( MultiCell(text='3.2-3.4',morecols=2) )
    cells.append( SimpleCell('3.5') )
    t.add_row(cells)

    cells = []
    cells.append( SimpleCell('4.1') )
    cells.append( MultiCell(text='4.2-5.2',morerows=1) )
    cells.append( MultiCell(text='4.3-5.4',morecols=1, morerows=1) )
    cells.append( SimpleCell('4.5') )
    t.add_row(cells)

    cells = []
    cells.append( SimpleCell('5.1') )
    cells.append( SimpleCell('5.5') )
    t.add_row(cells)

    print "---"
    print t.format()
