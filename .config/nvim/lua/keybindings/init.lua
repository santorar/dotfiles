vim.g.mapleader = " "
local mapper = function(mode,key,mapping)
vim.api.nvim_set_keymap(mode, key, mapping, {noremap = true, silent = true})
end

-- save the file
mapper('n', '<C-s>',":w<CR>")
-- duplicate the current line
mapper('n', '<Leader>t',':t.<CR>')
-- toggle the file tree
mapper('n', '<Leader>n',':NvimTreeToggle<CR>')
mapper('n', '<C-n>',':NvimTreeToggle<CR>')
-- update the plugins
mapper('n', '<Leader>uu',':PackerSync<CR>')

-- create new buffers
mapper('n', '<Leader>bt',':enew<CR>')
mapper('n', '<Leader>bh',':new<CR>')
mapper('n', '<Leader>bv',':vnew<CR>')

-- closes a buffer
mapper('n', '<Leader>qw',':bw<CR>')
mapper('n', '<Leader>qq',':bd!<CR>')

-- navigate on window splits
mapper ('n', '<C-h>','<C-w>h')
mapper ('n', '<C-j>','<C-w>j')
mapper ('n', '<C-k>','<C-w>k')
mapper ('n', '<C-l>','<C-w>l')

-- navigate on buffers
mapper('n', '<Leader>h',':BufferLineCyclePrev<CR>')
mapper('n', '<Leader>l',':BufferLineCycleNext<CR>')

-- split the window vertically
mapper('n', '<leader>sv',':vs<CR>')

-- split the window horizontally
mapper('n', '<Leader>sh',':split<CR>')

-- ident multiple lines
mapper('v', '>','>gv')
mapper('v', '<','<gv')
