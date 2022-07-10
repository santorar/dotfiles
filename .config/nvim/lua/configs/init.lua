local o = vim.o
local wo = vim.wo

-- global configs
o.fileencoding = 'utf-8'
o.clipboard = "unnamedplus"
o.lazyredraw = true
o.hidden = true
o.cursorline = true
o.whichwrap = 'b,s,<,>,[,],h,l'
o.pumheight = 10
o.termguicolors = true
o.splitright = true
o.showmode = false
o.scrolloff = 5

-- tab ident configuration
o.expandtab = true
o.tabstop = 4
o.shiftwidth = 4
o.softtabstop = 4
o.showtabline = 2

-- search configuration
o.hlsearch = true
o.ignorecase = true
o.smartcase = true

-- number config
o.relativenumber = true
o.number = true

-- mouse config
o.mouse = 'nvi'
